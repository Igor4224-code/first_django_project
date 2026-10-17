from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse

zodiak_dict: dict = {
    'aries': '<h1>Знак зодиака Овен</h1>',
    'taurus': '<h1>Знак зодиака Телец</h1>',
    'gemini': '<h1>Знак зодиака Близнецы</h1>',
    'cancer': '<h1>Знак зодиака Рак</h1>',
    'leo': '<h1>Знак зодиака Лев</h1>',
    'virgo': '<h1>Знак зодиака Дева</h1>',
    'libra': '<h1>Знак зодиака Весы</h1>',
    'scorpio': '<h1>Знак зодиака Скорпион</h1>',
    'sagittarius': '<h1>Знак зодиака Стрелец</h1>',
    'capricorn': '<h1>Знак зодиака Козерог</h1>',
    'aquaris': '<h1>Знак зодиака Водолей</h1>',
    'pisces': '<h1>Знак зодиака Рыбы</h1>',
}

zodiak_type_dict: dict = {'fire': ['aries', 'leo', 'sagittarius'],
    'earth': ['taurus', 'virgo', 'capricorn'],
    'air': ['gemini', 'leo', 'aquarius'],
    'water': ['cancer', 'scorpio', 'pisces']}


def index(request):
    sign_zodiak = list(zodiak_dict)
    temp_output = ''
    for sign in sign_zodiak:
        redirect_url = reverse('zodiak', args=(sign, ))
        temp_output += f'<li><a href="{redirect_url}"><h2>{sign.title()}</h2></a></li>'
    result_output = f'''
    <ul>
    {temp_output}
    </ul>
    '''
    return HttpResponse(result_output)


def get_zodiak(request, sign_zodiak: str):
    description = zodiak_dict.get(sign_zodiak, None)
    if description:
        return HttpResponse(description)
    else:
        return HttpResponseNotFound(f'Страница {sign_zodiak} не существует')


def get_zodiak_by_number(request, sign_zodiak: int):
    zodiak_list = list(zodiak_dict)
    if 0 < sign_zodiak < len(zodiak_list) + 1:
        name_zodiak = zodiak_list[sign_zodiak - 1]
        redirect_url = reverse('zodiak', args=(name_zodiak, ))
        return redirect(redirect_url)
    else:
        return HttpResponseNotFound(f'Страница {sign_zodiak} не существует')

def get_type(request, type_zodiak: str):
    if type_zodiak not in zodiak_type_dict:
        return HttpResponseNotFound(f'Страница {type_zodiak} не существует')

    temp_str = ''
    for sign in zodiak_type_dict[type_zodiak]:
        redirect_url = reverse('zodiak', args=(sign, ))
        temp_str += f'<li><a href="{redirect_url}"><h2>{sign.title()}</h2></a></li>'
    show_zodiaks = f'''<ul>{temp_str}</ul>'''
    return HttpResponse(show_zodiaks)

from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

zodiak_dict = {
    'zodiak': '<h1>Знак зодиака Овен</h1>',
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


def get_zodiak(request, sign_zodiak: str):
    descript = zodiak_dict.get(sign_zodiak, None)
    if descript:
        return HttpResponse(descript)
    else:
        return HttpResponseNotFound(f'Страница {sign_zodiak} не существует')

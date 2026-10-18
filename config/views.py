from django.http import HttpResponseNotFound
from django.shortcuts import render


def index(request):
    data: dict = {
        "title": "Главная страница",
        "menu": [
            {'title': "Доска объявлений", 'url_name': 'bboard'},
            {'title': "Гороскоп", 'url_name': 'home_horoscope'},
            {'title': "Известные женщины", 'url_name': 'home'},
        ]
    }
    return render(request, "index.html", context=data)


def page_not_found(request, exception):
    return HttpResponseNotFound("<h1>Страница не найдена</h1>")

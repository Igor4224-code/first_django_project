from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("<h1>Главная страница</h1>")


def categories(request, cats_id):
    return HttpResponse(f"<h1>Страница категорий</h1><p>Категория: {cats_id}</p>")


def categories_slug(request, cats_slug):
    return HttpResponse(f"<h1>Страница категорий</h1><p>Категория: {cats_slug}</p>")


def archive(request, year):
    return HttpResponse(f"<h1>Архив по годам</h1><p>Год: {year}</p>")

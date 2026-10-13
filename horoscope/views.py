from django.http import HttpResponse
from django.shortcuts import render


def aries(request):
    return HttpResponse('<h1>Знак зодиака Овен</h1>')


def taurus(request):
    return HttpResponse('<h1>Знак зодиака Телец</h1>')


def gemini(request):
    return HttpResponse('<h1>Знак зодиака Близнецы</h1>')


def cancer(request):
    return HttpResponse('<h1>Знак зодиака Рак</h1>')


def leo(request):
    return HttpResponse('<h1>Знак зодиака Лев</h1>')


def virgo(request):
    return HttpResponse('<h1>Знак зодиака Дева</h1>')


def libra(request):
    return HttpResponse('<h1>Знак зодиака Весы</h1>')


def scorpio(request):
    return HttpResponse('<h1>Знак зодиака Скорпион</h1>')


def sagittarius(request):
    return HttpResponse('<h1>Знак зодиака Стрелец</h1>')


def capricorn(request):
    return HttpResponse('<h1>Знак зодиака Козерог</h1>')


def aquaris(request):
    return HttpResponse('<h1>Знак зодиака Водолей</h1>')


def pisces(request):
    return HttpResponse('<h1>Знак зодиака Рыбы</h1>')

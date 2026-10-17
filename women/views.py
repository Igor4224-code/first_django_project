from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


def index(request):
    return render(request, 'women/index.html')


def about(request):
    return render(request, 'women/about.html')


def categories(request, cats_id):
    return HttpResponse(f"<h1>Страница категорий</h1><p>Категория: {cats_id}</p>")


def categories_slug(request, cats_slug):
    return HttpResponse(f"<h1>Страница категорий</h1><p>Категория: {cats_slug}</p>")


def archive(request, year):
    if year > 2027:
        redirect_url = reverse('cats_slug', args=('movies', ))
        return redirect(redirect_url)
    return HttpResponse(f"<h1>Архив по годам</h1><p>Год: {year}</p>")

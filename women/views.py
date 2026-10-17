from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse


class MyClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b


def index(request):
    data: dict = {
        'title': 'Главная страница',
        'menu': ['Главная', 'Все статьи', 'Добавить статью', 'Добавить комментарий'],
        'float': 34.28,
        'list': ['a', 'b', 'c', True, 34.28, None, [1, 2, 3], {'a': 1}, {'a': 1}],
        'dict': {'key_1': 'value_1', 'key_2': 'value_2', 'key_3': 'value_3'},
        'set': {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 2, 5},
        'obj': MyClass(10, 20),
}
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def categories(request, cats_id):
    return HttpResponse(f"<h1>Страница категорий</h1><p>Категория: {cats_id}</p>")


def categories_slug(request, cats_slug):
    return HttpResponse(f"<h1>Страница категорий</h1><p>Категория: {cats_slug}</p>")


def archive(request, year):
    if year > 2027:
        redirect_url = reverse('cats_slug', args=('movies', ))
        return redirect(redirect_url)
    return HttpResponse(f"<h1>Архив по годам</h1><p>Год: {year}</p>")

from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
        Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
        'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


def index(request):
    data: dict = {
        'title': 'Главная страница',
        'menu': ['Главная', 'Все статьи', 'Добавить статью', 'Добавить комментарий'],
        'posts': data_db,
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

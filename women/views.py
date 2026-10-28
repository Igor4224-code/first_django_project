from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .models import TagPost, Women, Category

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]

data_db = [
    {'id': 1, 'title': 'Анджелина Джоли', 'content': '''<h1>Анджелина Джоли</h1> (англ. Angelina Jolie[7], при рождении Войт (англ. Voight), ранее Джоли Питт (англ. Jolie Pitt); род. 4 июня 1975, Лос-Анджелес, Калифорния, США) — американская актриса кино, телевидения и озвучивания, кинорежиссёр, сценаристка, продюсер, фотомодель, посол доброй воли ООН.
        Обладательница премии «Оскар», трёх премий «Золотой глобус» (первая актриса в истории, три года подряд выигравшая премию) и двух «Премий Гильдии киноактёров США».''',
        'is_published': True},
    {'id': 2, 'title': 'Марго Робби', 'content': 'Биография Марго Робби', 'is_published': False},
    {'id': 3, 'title': 'Джулия Робертс', 'content': 'Биография Джулии Робертс', 'is_published': True},
]


def index(request):
    posts = Women.published.all()

    data: dict = {
        'title': 'Отображение по категориям',
        'posts': posts,
        'menu': menu,
        'cat_selected': 0,
}
    return render(request, 'women/index.html', context=data)


def about(request):
    return render(request, 'women/about.html', {'title': 'О сайте'})


def add_page(request):
    return HttpResponse('<h1>Добавление статьи</h1>')


def contact(request):
    return HttpResponse('<h1>Контакты</h1>')


def login(request):
    return HttpResponse('<h1>Авторизация</h1>')


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)
    data = {
        'title': post.title,
        'menu:': menu,
        'post': post,
        'cat_selected': 1,
    }
    return render(request, 'women/post.html', context=data)


def show_category(request, cat_slug):
    category = get_object_or_404(Category, slug=cat_slug)
    posts = Women.published.filter(cat_id=category.pk)

    data: dict = {
        'title': f'Рубрика: {category.name}',
        'posts': posts,
        'menu': menu,
        'cat_selected': category.pk,
}
    return render(request, 'women/index.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED)

    data = {
        'title': f'Тег: {tag.tag}',
        'posts': posts,
        'menu': menu,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)

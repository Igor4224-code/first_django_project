import os
import tempfile

from django.http import Http404, HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse

from .forms import AddPostForm, UploadFileForm
from .models import TagPost, Women, Category, UploadFiles

menu = [
    {'title': "О сайте", 'url_name': 'about'},
    {'title': "Добавить статью", 'url_name': 'add_page'},
    {'title': "Обратная связь", 'url_name': 'contact'},
    {'title': "Войти", 'url_name': 'login'}
]


def index(request):
    posts = Women.published.all().select_related('cat')

    data: dict = {
        'title': 'Отображение по категориям',
        'posts': posts,
        'menu': menu,
        'cat_selected': 0,
}
    return render(request, 'women/index.html', context=data)


# def handle_uploaded_file(f):
#     with open(f"uploads/{f.name}", "wb+") as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)


def about(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            UploadFiles(file=form.cleaned_data['file']).save()
    else:
        form = UploadFileForm()

    data = {
        'title': "О сайте",
        'menu': menu,
        'form': form,
    }

    return render(request, 'women/about.html', context=data)


def add_page(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    data = {
        'menu': menu,
        'title': 'Добавление статьи',
        'form': form
    }
    return render(request, 'women/addpage.html', context=data)


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
    posts = Women.published.filter(cat_id=category.pk).select_related('cat')

    data: dict = {
        'title': f'Рубрика: {category.name}',
        'posts': posts,
        'menu': menu,
        'cat_selected': category.pk,
}
    return render(request, 'women/index.html', context=data)


def show_tag_postlist(request, tag_slug):
    tag = get_object_or_404(TagPost, slug=tag_slug)
    posts = tag.tags.filter(is_published=Women.Status.PUBLISHED).select_related('cat')

    data = {
        'title': f'Тег: {tag.tag}',
        'posts': posts,
        'menu': menu,
        'cat_selected': None,
    }

    return render(request, 'women/index.html', context=data)

from django.urls import path, register_converter
from . import converters
from . import views


register_converter(converters.ForDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='index'),
    path('cats/<int:cats_id>/', views.categories, name='cats'),
    path('cats/<slug:cats_slug>/', views.categories_slug, name='cats_slug'),
    path('archive/<year4:year>/', views.archive, name='year'),
]

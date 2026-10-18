from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home_horoscope'),
    path('<int:sign_zodiak>/', views.get_zodiak_by_number, name='zodiak_num'),
    path('<str:sign_zodiak>/', views.get_zodiak, name='zodiak'),
    path('type/<str:type_zodiak>/', views.get_type, name='type'),
]

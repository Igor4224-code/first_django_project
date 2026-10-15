from django.urls import path
from . import views

urlpatterns = [
    path('<int:sign_zodiak>/', views.get_zodiak_by_number, name='zodiak_num'),
    path('<str:sign_zodiak>/', views.get_zodiak, name='zodiak'),
]

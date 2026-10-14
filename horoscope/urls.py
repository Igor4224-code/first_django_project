from django.urls import path
from . import views

urlpatterns = [
    path('<str:sign_zodiak>/', views.get_zodiak, name='sign_zodiak'),
]

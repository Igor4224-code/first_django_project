from django.urls import path
from . import views

urlpatterns = [
    path('aries/', views.aries, name='aries'),
    path('taurus/', views.taurus, name='taurus'),
    path('gemini/', views.gemini, name='gemini'),
    path('cancer/', views.cancer, name='cancer'),
    path('leo/', views.leo, name='leo'),
    path('virgo/', views.virgo, name='virgo'),
    path('libra/', views.libra, name='libra'),
    path('scorpio/', views.scorpio, name='scorpio'),
    path('sagittarius/', views.sagittarius, name='sagittarius'),
    path('capricorn/', views.capricorn, name='capricorn'),
    path('aquaris/', views.aquaris, name='aquaris'),
    path('pisces/', views.pisces, name='pisces'),
]

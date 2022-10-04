from django.urls import path
from . import views

urlpatterns = [
    path('', views.zodiac, name='zodiac'),
    path('arias', views.arias, name='arias'),
    path('taurus', views.taurus, name='taurus'),
    path('gemini', views.gemini, name='gemini'),
    path('cancer', views.cancer, name='cancer'),
    path('leo', views.leo, name='leo'),
    path('virgo', views.virgo, name='virgo'),
    path('libra', views.libra, name='libra'),
    path('scorpius', views.scorpius, name='scorpius'),
    path('sagittarius', views.sagittarius, name='sagittarius'),
    path('capricornus', views.capricornus, name='capricornus'),
    path('aquarius', views.aquarius, name='aquarius'),
    path('pisces', views.pisces, name='pisces'),
]

from django.shortcuts import render
from .models import Horoscope


def zodiac(request):
    prediction = Horoscope.objects.all()
    data = {
        'title': 'Гороскоп на сегодня',
        'values': ['Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион',
                   'Стрелец', 'Козерог', 'Водолей', 'Рыбы']
    }
    return render(request, 'zodiac/zodiac.html', data, {'prediction': prediction})

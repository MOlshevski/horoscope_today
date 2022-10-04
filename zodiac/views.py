from django.shortcuts import render
from .models import Horoscope
from random import randint


def zodiac(request):
    return render(request, 'zodiac/zodiac.html')


def arias(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/arias.html', {'prediction': prediction})


def taurus(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/taurus.html', {'prediction': prediction})


def gemini(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/gemini.html', {'prediction': prediction})


def cancer(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/cancer.html', {'prediction': prediction})


def leo(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/leo.html', {'prediction': prediction})


def virgo(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/virgo.html', {'prediction': prediction})


def libra(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/libra.html', {'prediction': prediction})


def scorpius(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/scorpius.html', {'prediction': prediction})


def sagittarius(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/sagittarius.html', {'prediction': prediction})


def capricornus(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/capricornus.html', {'prediction': prediction})


def aquarius(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/aquarius.html', {'prediction': prediction})


def pisces(request):
    prediction = Horoscope.objects.all().order_by('-date')
    return render(request, 'zodiac/pisces.html', {'prediction': prediction})

""" Создаю функцию для создания рандомного гороскопа для знаков зодиака, чтобы наполнить базу данных"""


def random_prediction():
    arr1 = ["благоприятный", "неблагоприятный"]
    arr2 = ["инвестиций", "продуктивной работы", "встречи с друзьями", "свидания"]

    a1 = arr1[randint(0, 1)]
    a2 = arr2[randint(0, 3)]

    if a1 == 'благоприятный':
        a3 = 'Не сидите дома'
    elif a1 == "неблагоприятный":
        a3 = 'Останьтесь дома'
    gen = f'Сегодня у Вас {a1} день для {a2}. {a3}.'
    return gen


zodiac_signs = [
        'Овен', 'Телец', 'Близнецы', 'Рак', 'Лев', 'Дева', 'Весы', 'Скорпион', 'Стрелец', 'Козерог', 'Водолей', 'Рыбы'
    ]

#Цикл для наполнения БД. меняю дату и выполняю наполнение БД.
'''for i in range(len(zodiac_signs)):  
    Horoscope.objects.create(sign=zodiac_signs[i], horoscope_text=random_prediction(), date='2022-10-04')'''

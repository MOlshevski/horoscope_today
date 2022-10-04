from django.db import models


class Horoscope(models.Model):
    sign = models.CharField('Знак зодиака', max_length=20)
    horoscope_text = models.TextField('Гороскоп')
    date = models.DateField('Дата', max_length=15)

    def __str__(self):
        return ' '.join([
            self.sign,
            self.horoscope_text
            ])

    class Meta:
        verbose_name = 'Гороскопы'
        verbose_name_plural = 'Гороскоп'



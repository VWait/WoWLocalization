from django.db import models


class Card(models.Model):
    name_ru = models.CharField('Имя', max_length=50)
    name_en = models.CharField('Name', max_length=50)
    cost = models.IntegerField('Стоимость')


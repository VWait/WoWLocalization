from django.db import models


class Card(models.Model):
    name_ru = models.CharField('Имя-рус', max_length=50, default='-')
    name_en = models.CharField('Имя-англ', max_length=50, default='-')
    cost = models.IntegerField('Стоимость', default=0)
    faction = models.CharField('Фракция', max_length=50, default='-')
    class_card = models.CharField('Класс', max_length=50, default='-')
    number = models.IntegerField('Номер', default=0)
    rarity_ru = models.CharField('Редкость-рус', max_length=50, default='-')
    rarity_en = models.CharField('Редкость-англ', max_length=50, default='-')
    type_ru = models.CharField('Тип-рус', max_length=100, default='-')
    type_en = models.CharField('Тип-англ', max_length=100, default='-')
    atk = models.IntegerField('ATK', default=0)
    atk_type = models.CharField('Тип ATK', max_length=50, default='-')
    health = models.IntegerField('Здоровье', default=0)
    strike_cost = models.IntegerField('Стоимость удара', default=0)
    def_card = models.IntegerField('БРН', default=0)
    capacity = models.IntegerField('Вместимость', default=0)
    ability_en = models.TextField('Способность-англ', default='-')
    ability_ru = models.TextField('Способность-рус', default='-')
    fluff_en = models.TextField('ХудожественныйТекст-англ', default='-')
    fluff_ru = models.TextField('ХудожественныйТекст-рус', default='-')
    artist = models.CharField('Художник', max_length=50, default='-')
    faq_en = models.TextField('Примечание-англ', default='-')
    faq_ru = models.TextField('Примечание-рус', default='-')
    legality_core = models.CharField('Core', max_length=50, default='-')
    legality_block = models.CharField('Block', max_length=50, default='-')
    legality_contemporary = models.CharField('Contemporary', max_length=50, default='-')
    legality_classic = models.CharField('Classic', max_length=50, default='-')
    block = models.IntegerField('Блок', default=0)
    set_en = models.CharField('Выпуск-англ', max_length=50, default='-')
    set_ru = models.CharField('Выпуск-рус', max_length=50, default='-')
    released = models.CharField('Дата выпуска', max_length=20, default='-')


class SimpleSearchRequest(models.Model):
    text = models.CharField('Текст', max_length=50)

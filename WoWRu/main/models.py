from django.db import models


class Card(models.Model):
    name_en = models.CharField('Имя-англ', max_length=50, default=None, null=True)
    name_ru = models.CharField('Имя-рус', max_length=50, default=None, null=True)
    cost = models.IntegerField('Стоимость', default=None, null=True)
    faction = models.CharField('Фракция', max_length=50, default=None, null=True)
    class_card = models.CharField('Класс', max_length=50, default=None, null=True)
    number = models.IntegerField('Номер', default=None, null=True)
    rarity_en = models.CharField('Редкость-англ', max_length=50, default=None, null=True)
    rarity_ru = models.CharField('Редкость-рус', max_length=50, default=None, null=True)
    type_en = models.CharField('Тип-англ', max_length=100, default=None, null=True)
    type_ru = models.CharField('Тип-рус', max_length=100, default=None, null=True)
    atk = models.IntegerField('ATK', default=None, null=True)
    atk_type = models.CharField('Тип ATK', max_length=50, default=None, null=True)
    health = models.IntegerField('Здоровье', default=None, null=True)
    strike_cost = models.IntegerField('Стоимость удара', default=None, null=True)
    def_card = models.IntegerField('БРН', default=None, null=True)
    capacity = models.IntegerField('Вместимость', default=None, null=True)
    ability_en = models.TextField('Способность-англ', default=None, null=True)
    ability_ru = models.TextField('Способность-рус', default=None, null=True)
    fluff_en = models.TextField('ХудожественныйТекст-англ', default=None, null=True)
    fluff_ru = models.TextField('ХудожественныйТекст-рус', default=None, null=True)
    artist = models.CharField('Художник', max_length=50, default=None, null=True)
    faq_en = models.TextField('Примечание-англ', default=None, null=True)
    faq_ru = models.TextField('Примечание-рус', default=None, null=True)
    legality_core = models.CharField('Core', max_length=50, default=None, null=True)
    legality_block = models.CharField('Block', max_length=50, default=None, null=True)
    legality_contemporary = models.CharField('Contemporary', max_length=50, default=None, null=True)
    legality_classic = models.CharField('Classic', max_length=50, default=None, null=True)
    block = models.IntegerField('Блок', default=None, null=True)
    set_en = models.CharField('Выпуск-англ', max_length=50, default=None, null=True)
    set_ru = models.CharField('Выпуск-рус', max_length=50, default=None, null=True)
    released = models.CharField('Дата выпуска', max_length=20, default=None, null=True)


class SimpleSearchRequest(models.Model):
    text = models.CharField('Текст', max_length=50)

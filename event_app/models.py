from django.db import models
from enum import Enum


class TypeChoice(Enum):
    ONE = 'Разовое мероприятие'
    PER = 'Периодическое мероприятие'


class PeriodChoice(Enum):
    DAY = 'Ежедневное'
    MTH = 'Ежемесячное'
    YER = 'Ежегодное'


class Prices(models.Model):
    price = models.IntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.price)


class Town(models.Model):
    name = models.CharField(max_length=250)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.name)


class Day(models.Model):
    name = models.PositiveIntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.name)


class Month(models.Model):
    name = models.PositiveIntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.name)


class Year(models.Model):
    name = models.PositiveIntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.name)


class Tickets(models.Model):
    number = models.PositiveIntegerField()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.number)


class EventBase(models.Model):
    name = models.CharField(max_length=50)
    event_type = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in TypeChoice],
                                  default=TypeChoice.ONE)
    event_period = models.CharField(max_length=10, choices=[(tag.name, tag.value) for tag in PeriodChoice], blank=True,
                                    null=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.name)


class Event(models.Model):
    base = models.ForeignKey('EventBase', related_name='event', on_delete=models.PROTECT)
    price = models.ForeignKey('Prices', related_name='event', on_delete=models.PROTECT)
    town = models.ForeignKey('Town', related_name='event', on_delete=models.PROTECT)
    day = models.ForeignKey('Day', related_name='event', on_delete=models.PROTECT)
    month = models.ForeignKey('Month', related_name='event', on_delete=models.PROTECT)
    year = models.ForeignKey('Year', related_name='event', on_delete=models.PROTECT)
    start_time = models.TimeField(blank=True, null=True)
    tickets_total = models.ForeignKey('Tickets', related_name='event', on_delete=models.PROTECT)
    tickets_bought = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ('id',)

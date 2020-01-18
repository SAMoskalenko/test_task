from django.contrib import admin
from .models import (Prices,
                     Town,
                     Day,
                     Month,
                     Year,
                     Tickets,
                     EventBase,
                     Event)


@admin.register(Prices)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'price']
    ordering = ['id']
    search_fields = ['price']


@admin.register(Town)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Day)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Month)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Year)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    ordering = ['id']
    search_fields = ['name']


@admin.register(Tickets)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']
    ordering = ['id']
    search_fields = ['number']


@admin.register(EventBase)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'event_type', 'event_period']
    ordering = ['id']
    search_fields = ['name', 'event_type', 'event_period']


@admin.register(Event)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id', 'base', 'price', 'town', 'day', 'month', 'year', 'start_time', 'tickets_total',
                    'tickets_bought']
    ordering = ['id']
    search_fields = ['name', 'base', 'price', 'town', 'day', 'month', 'year', 'start_time', 'tickets_total',
                     'tickets_bought']

from django_filters import rest_framework as filters
from .models import (
                     Event)


class EventFilter(filters.FilterSet):
    town_filter = filters.CharFilter(field_name='town__name', lookup_expr='contains')
    month_filter = filters.CharFilter(field_name='month__name', lookup_expr='contains')
    event_name_filter = filters.CharFilter(field_name='base__name', lookup_expr='contains')

    class Meta:
        model = Event
        fields = ['town_filter', 'month_filter', 'event_name_filter']


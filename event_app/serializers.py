from rest_framework import serializers
from .models import (Event)
from .exeptions import (EventException,
                        ERR_BUYING,
                        ERR_WRONG_EVENT)


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = '__all__'
        depth = 2


class BoughtTicketsSerializer(serializers.ModelSerializer):
    event_name = serializers.CharField(write_only=True, max_length=250)
    event_year = serializers.IntegerField(write_only=True)
    event_month = serializers.IntegerField(write_only=True)
    event_day = serializers.IntegerField(write_only=True)
    number_of_tickets = serializers.IntegerField(write_only=True)

    class Meta:
        model = Event
        fields = '__all__'
        read_only_fields = (
            'id', 'base', 'price', 'town', 'day', 'month', 'year', 'start_time', 'tickets_total', 'tickets_bought')
        depth = 2

    def create(self, validated_data):
        try:
            e = Event.objects.get(base__name=validated_data.get('event_name'),
                                  year__name=validated_data.get('event_year'),
                                  month__name=validated_data.get('event_month'),
                                  day__name=validated_data.get('event_day'))
        except:
            raise EventException(**ERR_WRONG_EVENT)
        total = e.tickets_total
        bought = e.tickets_bought + validated_data.get('number_of_tickets')
        if total.number >= bought:
            e.tickets_bought += validated_data.get('number_of_tickets')
            e.save()
            return {}
        else:
            raise EventException(**ERR_BUYING)

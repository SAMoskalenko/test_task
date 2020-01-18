from django_filters import rest_framework as filters
from rest_framework import viewsets
from rest_framework.mixins import (ListModelMixin, CreateModelMixin)

from .models import (Event)
from .serializers import (EventSerializer,
                          BoughtTicketsSerializer)
from .filters import (EventFilter)


class EventViewSet(ListModelMixin, viewsets.GenericViewSet):
    """
    Return events
    """

    serializer_class = EventSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = EventFilter

    def get_queryset(self):
        return Event.objects.all()


class BoughtTicketsViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """
    Bought tickets
    """

    serializer_class = BoughtTicketsSerializer

    def get_queryset(self):
        return Event.objects.all()

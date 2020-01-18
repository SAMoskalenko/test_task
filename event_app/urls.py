from rest_framework.routers import DefaultRouter

from .views import (EventViewSet,
                    BoughtTicketsViewSet)

router = DefaultRouter()

router.register(r'', EventViewSet, basename='event')
router.register(r'bougth_tickets', BoughtTicketsViewSet, basename='bougth_tickets')

urlpatterns = router.urls

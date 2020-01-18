import json

from django.core.management import call_command
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient


class TestEvent(APITestCase):

    def setUp(self):
        call_command('loaddata', 'db.json')

        self.client = APIClient()

    def test_events(self):
        # проверка get
        url = reverse('event-list')
        response = self.client.get(url, {}, format='json')
        content = json.loads(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # проверка post tickets OK
        data = {'event_name': content['results'][0]['base']['name'],
                'event_year': content['results'][0]['year']['name'],
                'event_month': content['results'][0]['month']['name'],
                'event_day': content['results'][0]['day']['name'],
                'number_of_tickets': 0
                }
        url = reverse('bougth_tickets-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # проверка post tickets 400
        data = {'event_name': content['results'][0]['base']['name'],
                'event_year': content['results'][0]['year']['name'],
                'event_month': content['results'][0]['month']['name'],
                'event_day': 28,
                'number_of_tickets': 0
                }
        url = reverse('bougth_tickets-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # проверка post tickets 400
        data = {'event_name': content['results'][0]['base']['name'],
                'event_year': content['results'][0]['year']['name'],
                'event_month': content['results'][0]['month']['name'],
                'event_day': content['results'][0]['day']['name'],
                'number_of_tickets': 1
                }
        url = reverse('bougth_tickets-list')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def tearDown(self):
        call_command('sqlsequencereset', 'event_app')

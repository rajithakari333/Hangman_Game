from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

class HangmanAPITestCase(APITestCase):
    def test_start_new_game(self):
        url = reverse('new_game')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue('id' in response.data)

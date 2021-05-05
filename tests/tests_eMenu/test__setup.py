'''
for Django inbuilt testing set up class to test views
'''

from rest_framework.test import APITestCase
from django.urls import reverse
from faker import Faker
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
import random


class TestDishApiSetUp(APITestCase):

    # run before testing
    def setUp(self):
        self.get_dish_url = reverse('eMenuAPI:retrieve_dish_details', kwargs={'pk': '1'})
        self.create_dish_url = reverse('eMenuAPI:create-dish')
        self.update_dish_url = reverse('eMenuAPI:update-delete-dish', kwargs={'pk': '1'})
        self.delete_dish_url = reverse('eMenuAPI:update-delete-dish', kwargs={'pk': '1'})
        self.fake = Faker()

        self.user_instance = User.objects.create(username='MickyMouse', password='sophisticated-pws-123')
        self.user_token_instance = Token.objects.create(user=self.user_instance)

        self.user_data = {
            'name': self.fake.text(max_nb_chars=60),
            'description': self.fake.text(max_nb_chars=200),
            'price_in_dollars': 25,
            'minutes_to_prepare': 15,
            'is_vegetarian': random.choice([True, False])
        }
        
        return super().setUp()

    # authenticate user if needed
    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {self.user_token_instance.key}")

    # run after testing
    def tearDown(self):
        return super().tearDown()
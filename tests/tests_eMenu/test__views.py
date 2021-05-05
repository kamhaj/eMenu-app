'''
test api views
'''

from .test__setup import TestDishApiSetUp
from rest_framework import status


class TestDishApiViews(TestDishApiSetUp):

    ## Test GET
    ## TODO - test_user_cannot_get_dish_with_no_data (pk)
    ## TODO - test_user_can_get_dish_with_data
    
    ## Test POST method
    def test_user_cannot_create_dish_with_no_data(self):
        response = self.client.post(self.create_dish_url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_user_cannot_create_dish_with_no_authentication(self):
        response = self.client.post(self.create_dish_url, self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_can_create_dish_with_data_and_authentication(self):
        self.api_authentication()
        response = self.client.post(self.create_dish_url, self.user_data, format='json')
        self.assertEqual(response.data['name'], self.user_data['name'])
        self.assertEqual(response.data['description'], self.user_data['description'])
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    
    ## Test PUT
    ## TODO - test_user_cannot_update_dish_with_no_data (pk, title, content)
    ## TODO - test_user_cannot_update_dish_with_no_authentication (token)
    ## TODO - test_user_can_update_dish_with_data_and_authentication 

    ## Test DELETE
    ## TODO - test_user_cannot_delete_dish_with_no_data (pk)
    ## TODO - test_user_cannot_delete_dish_with_no_authentication (token)
    ## TODO - test_user_can_delete_dish_with_data_and_authentication



## TODO write similar class for Menu API
#class TestMenuApiViews(TestMenuAPISetUp):
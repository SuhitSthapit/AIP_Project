from django.test import TestCase
from .models import Liquor
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse

class ModelTestCase(TestCase):
    """This class defines the test suite for the liquor model."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.liquor_name = "Write quality code"
        self.liquor = Liquor(name=self.liquor_name)

    def test_model_can_create_a_liquor(self):
        """Test the liquor model can create a liquor."""
        old_count = Liquor.objects.count()
        self.liquor.save()
        new_count = Liquor.objects.count()
        self.assertNotEqual(old_count, new_count)

class ViewTestCase(TestCase):
    """Test suite for the api views."""

    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()
        self.liquor_data = {'name': 'Gorkha'}
        self.response = self.client.post(
            reverse('create'),
            self.liquor_data,
            format="json")

    def test_api_can_create_a_liquor(self):
        """Test the api has liquor creation capability."""
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    
    def test_api_can_get_a_liquor(self):
        """Test the api can get a given liquor."""
        liquor = Liquor.objects.get()
        response = self.client.get(
            reverse('details'),
            kwargs={'pk': liquor.id}, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, liquor)

    def test_api_can_update_liquor(self):
        """Test the api can update a given liquor."""
        change_liquor = {'name': 'New Whisky'}
        res = self.client.put(
            reverse('details', kwargs={'pk': liquor.id}),
            change_liquor, format='json'
        )
        #print (liquor.id)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_api_can_delete_liquor(self):
        """Test the api can delete a bucketlist."""
        liquor = Liquor.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': liquor.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
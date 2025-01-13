from django.test import TestCase, RequestFactory,SimpleTestCase, Client
from django.urls import reverse,resolve
from decimal import Decimal
# Create your tests here.
from .views import (all_stat)



"""
#test unitaire url.py

class StatistiqueURLTest(TestCase):

    def test_statistique_url_resolves_to_all_stat_view(self):
        url = reverse('StatApp:statistique')
        self.assertEqual(resolve(url).func, all_stat)


#test unitaire views.py
class AllStatTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('StatApp:statistique')

    def test_all_stat_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)


"""
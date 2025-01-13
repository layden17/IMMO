from django.test import TestCase, RequestFactory,SimpleTestCase, Client
from django.urls import reverse,resolve
from decimal import Decimal
from django.core.files.uploadedfile import SimpleUploadedFile

from VenteApp.models import Article
from .forms import ClientForms
from ProduitApp.models import Produit
from ProduitApp.forms import Produit,ProduitBrut,ProduitBrutForm,AutreProduit,AutreProduitForm
from .models import Client
from .views import creerArticle, createCustomer, updateCustomer, index, deleteCustomer, searchBar, render_to_pdf, \
    ViewPDF


#test unitaire models.py
class ClientTest(TestCase):

    def setUp(self):
        self.client = Client.objects.create(
            prenom="Jean",
            nom="Dupont",
            email="jean.dupont@example.com",
            type="Particulier",
            adresse="123 rue des fleurs",
            tel="0123456789",
            dette=Decimal('100.00'),
            piece_ID=None
        )

    def test_str(self):
        self.assertEqual(str(self.client), "Jean Dupont")

    def test_dette_default_value(self):
        client = Client.objects.create(
            prenom="Luc",
            nom="Martin",
            email="luc.martin@example.com",
            type="Particulier",
            adresse="456 avenue des étoiles",
            tel="0123456789"
        )
        self.assertEqual(client.dette, Decimal('0'))

    def test_verbose_names(self):
        self.assertEqual(Client._meta.verbose_name, "Client")
        self.assertEqual(Client._meta.verbose_name_plural, "Clients")



#test unitaires de urls.py
class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('ClientApp:clientApp')
        self.assertEqual(resolve(url).func, index)

    def test_create_customer_url_resolves(self):
        url = reverse('ClientApp:create_customer')
        self.assertEqual(resolve(url).func, createCustomer)

    def test_update_customer_url_resolves(self):
        url = reverse('ClientApp:update_customer', args=['1'])
        self.assertEqual(resolve(url).func, updateCustomer)

    def test_delete_customer_url_resolves(self):
        url = reverse('ClientApp:delete_customer', args=['1'])
        self.assertEqual(resolve(url).func, deleteCustomer)

    def test_searchBar_url_resolves(self):
        url = reverse('ClientApp:searchClient')
        self.assertEqual(resolve(url).func, searchBar)




#test unitaire views.py

class IndexViewTest(TestCase):
    def test_index_view_post(self):
        # Crée un objet ClientForms valide.
        data = {
            'prenom': 'Jean',
            'nom': 'Dupont',
            'email': 'jean.dupont@example.com',
            'type': 'Particulier',
            'adresse': '123 rue des fleurs',
            'tel': '0123456789',
            'dette': '100.00',
        }
        form = ClientForms(data=data)
        self.assertTrue(form.is_valid())


class CustomerCreationTestCase(TestCase):
    def setUp(self):
        self.url = reverse('ClientApp:create_customer')
        self.valid_data = {
            'prenom': 'John',
            'nom': 'Doe',
            'email': 'johndoe@example.com',
            'type': 'Particulier',
            'adresse': '123 Main St',
            'tel': '123456789',
            'dette': 0,

        }
    def test_customer_creation_with_valid_data(self):
        """
        Test customer creation with valid form data
        """
        response = self.client.post(self.url, data=self.valid_data)
        self.assertEqual(response.status_code, 302)  # Check redirection to success page
        self.assertEqual(Client.objects.count(), 1)  # Check that a new customer object was created

        client = Client.objects.first()
        self.assertEqual(client.prenom, 'John')
        self.assertEqual(client.nom, 'Doe')
        self.assertEqual(client.email, 'johndoe@example.com')
        self.assertEqual(client.type, 'Particulier')
        self.assertEqual(client.adresse, '123 Main St')
        self.assertEqual(client.tel, '123456789')
        self.assertEqual(client.dette, 0)
        self.assertIsNotNone(client.piece_ID)

    def test_customer_creation_with_invalid_data(self):
        """
        Test customer creation with invalid form data
        """
        response = self.client.post(self.url, data={})  # Empty data should be invalid
        self.assertEqual(response.status_code, 200)  # Check that the form is not submitted
        self.assertFalse(Client.objects.exists())  # Check that no customer object was created

        form = response.context['form']
        self.assertIsInstance(form, ClientForms)  # Check that the context contains the form instance
        self.assertTrue(form.errors)  # Check that the form is invalid



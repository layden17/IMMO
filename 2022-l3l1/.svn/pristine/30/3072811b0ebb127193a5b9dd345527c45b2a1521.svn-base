from django.test import TestCase
from django.test import TestCase, RequestFactory,SimpleTestCase, Client
from django.urls import reverse,resolve
from decimal import Decimal

from .views import ajout_fournisseurs,index,Fournisseurs, FournisseurDeleteView,FournisseurUpdateView,FournisseurForm,Facture,search_fournisseurs,tri_fournisseurs,factures_detail
# Create your tests here.

#test unitaire de urls.py
class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('FournisseursApp:fournisseurs')
        self.assertEqual(resolve(url).func, index)

    def test_ajout_fournisseurs_url_resolves(self):
        url = reverse('FournisseursApp:ajout_fournisseurs')
        self.assertEqual(resolve(url).func, ajout_fournisseurs)

    def test_supprimer_fournisseur_url_resolves(self):
        url = reverse('FournisseursApp:supprimer_fournisseur', args=[1])
        self.assertEqual(resolve(url).func.view_class, FournisseurDeleteView)

    def test_modifier_fournisseur_url_resolves(self):
        url = reverse('FournisseursApp:modifier_fournisseur', args=[1])
        self.assertEqual(resolve(url).func.view_class, FournisseurUpdateView)

    def test_search_fournisseurs_url_resolves(self):
        url = reverse('FournisseursApp:search_fournisseurs')
        self.assertEqual(resolve(url).func, search_fournisseurs)

    def test_tri_fournisseurs_url_resolves(self):
        url = reverse('FournisseursApp:tri_fournisseurs', args=['nom'])
        self.assertEqual(resolve(url).func, tri_fournisseurs)

    def test_factures_detail_url_resolves(self):
        url = reverse('FournisseursApp:factures_detail', args=[1])
        self.assertEqual(resolve(url).func, factures_detail)


#test models.py
class FournisseursModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Fournisseurs.objects.create(Raison_social='Fournisseur A', email='fournisseurA@example.com', Numero_Telephone='+33123456789', Fax='+33123456789', Versement=0, Dette=0)

    def test_Raison_social_label(self):
        fournisseur = Fournisseurs.objects.get(id=1)
        field_label = fournisseur._meta.get_field('Raison_social').verbose_name
        self.assertEqual(field_label, 'Raison social')

    def test_email_max_length(self):
        fournisseur = Fournisseurs.objects.get(id=1)
        max_length = fournisseur._meta.get_field('email').max_length
        self.assertEqual(max_length, 100)


    def test_Fax_null(self):
        fournisseur = Fournisseurs.objects.get(id=1)
        null_allowed = fournisseur._meta.get_field('Fax').null
        self.assertTrue(null_allowed)



#test unitaire views.py

class TestAjoutFournisseurs(TestCase):

    def setUp(self):
        self.client = Client()
        self.url = reverse('ajout_fournisseurs')
        self.valid_payload = {
            'Raison_social': 'Fournisseur Test',
            'email': 'test@example.com',
            'Numero_Telephone': '+33123456789',
            'Versement': 1000,
            'Dette': 500,
        }
        self.invalid_payload = {
            'Raison_social': '',
            'email': 'invalid-email',
            'Numero_Telephone': '12345',
            'Versement': -1000,
            'Dette': -500,
        }
        self.valid_form = FournisseurForm(data=self.valid_payload)
        self.invalid_form = FournisseurForm(data=self.invalid_payload)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ajout_fournisseurs.html')
        self.assertIsInstance(response.context['fournisseur_form'], FournisseurForm)


    def test_post_invalid_form(self):
        response = self.client.post(self.url, self.invalid_payload)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ajout_fournisseurs.html')
        self.assertIsInstance(response.context['fournisseur_form'], FournisseurForm)
        self.assertFalse(Fournisseurs.objects.filter(Raison_social=self.invalid_payload['Raison_social']).exists())



    class FournisseurDeleteViewTestCase(TestCase):
        def setUp(self):
            self.fournisseur = Fournisseurs.objects.create(Raison_social="Test Inc.", email="test@test.com", Numero_Telephone="+1234567890")
            self.url = reverse('FournisseursApp:delete_fournisseur', kwargs={'pk': self.fournisseur.pk})
            self.client = Client()

        def test_delete_fournisseur(self):
            response = self.client.post(self.url)
            self.assertEqual(response.status_code, 302)
            self.assertEqual(Fournisseurs.objects.count(), 0)
            self.assertRedirects(response, reverse('FournisseursApp:fournisseurs'))




from django.test import TestCase, RequestFactory,SimpleTestCase, Client
from django.urls import reverse,resolve
from decimal import Decimal
# Create your tests here.

from .models import Categorie,Produit, AutreProduit, CategorieFer,ProduitBrut,HistoriquePrixAchatQuintal,HistoriquePrixVenteQuintal, Cadre
from .forms import CategorieForm, CadreForms, AutreProduitForm, ProduitBrutForm
from .views import (produit_brut, modifier_produit, historique_prix_achat_quintal, historique_prix_vente_quintal,
                    autre_produit, modifier_autre_produit, add_autre_produit, autre_produit_detail, supprimer_autre_produit, recherche_autre_produit,
                    cadre, createCadre, supprimer_cadre, modifier_cadre, tri_cadre,
                    index, categorie, create_category, modifier_categorie, supprimer_categorie)


# test unitaire models.py
class CategorieFormTest(TestCase):
    def test_valid_form(self):
        """
        Teste la validation d'un formulaire valide.
        """
        data = {'name': 'Nouvelle catégorie'}
        form = CategorieForm(data=data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """
        Teste la non-validation d'un formulaire avec des données manquantes.
        """
        data = {}
        form = CategorieForm(data=data)
        self.assertFalse(form.is_valid())


# test unitaire création produit brut
class ProduitBrutTestCase(TestCase):

    def setUp(self):
        # créer une catégorie 'produit brut'
        categorie = Categorie.objects.create(name='produit brut')

        # créer un produit brut avec les valeurs de test
        produit_brut = ProduitBrut.objects.create(
            categorie=categorie,
            type_fer='Fer /6',
            stock_quintal=10,
            stock_barre=20,
            stock_metre=30,
            prix_quintal=100,
            prix_metre=50,
            prix_barre=10,
            prix_achat_quintal=80,
            prix_achat_barre=8,
            prix_achat_metre=40
        )

        self.produit_brut = produit_brut

    def test_produit_brut_creation(self):
        # tester que l'instance de produit brut a bien été créée
        self.assertIsInstance(self.produit_brut, ProduitBrut)


# test unitaire création cadre
class CadreTestCase(TestCase):
    def setUp(self):
        self.cadre = Cadre.objects.create(cadre_choix='Cadre')

    def test_cadre_creation(self):
        cadre = self.cadre
        self.assertTrue(isinstance(cadre, Cadre))
        self.assertEqual(cadre.__str__(), cadre.cadre_choix)



# test unitaire création autre produit
class AutreProduitTestCase(TestCase):

    def setUp(self):
        self.categorie = Categorie.objects.create(name='Catégorie de test')
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=self.categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )

    def test_autre_produit_attributes(self):
        self.assertEqual(self.autre_produit.designation, 'Test produit')
        self.assertEqual(self.autre_produit.description, 'Description de test')
        self.assertEqual(self.autre_produit.TVA, 20)
        self.assertEqual(self.autre_produit.categorie, self.categorie)
        self.assertEqual(self.autre_produit.prix_vente, 10.50)
        self.assertEqual(self.autre_produit.prix_achat, 5.00)
        self.assertEqual(self.autre_produit.quantite, 10.00)
        self.assertEqual(self.autre_produit.stock_alerte, 5.00)

    def test_autre_produit_str(self):
        self.assertEqual(str(self.autre_produit), 'Test produit')



# test unitaire de urls.py
class TestUrls(SimpleTestCase):

    def test_produit_brut_url_resolves(self):
        url = reverse('ProduitApp:produit_brut')
        self.assertEquals(resolve(url).func, produit_brut)

    def test_modifier_produit_url_resolves(self):
        url = reverse('ProduitApp:modifier_produit', args=[1])
        self.assertEquals(resolve(url).func.view_class, modifier_produit)

    def test_historique_prix_achat_quintal_url_resolves(self):
        url = reverse('ProduitApp:historique_prix_achat_quintal')
        self.assertEquals(resolve(url).func, historique_prix_achat_quintal)

    def test_historique_prix_vente_quintal_url_resolves(self):
        url = reverse('ProduitApp:historique_prix_vente_quintal')
        self.assertEquals(resolve(url).func, historique_prix_vente_quintal)

    def test_autre_produit_url_resolves(self):
        url = reverse('ProduitApp:autre_produit')
        self.assertEquals(resolve(url).func, autre_produit)

    def test_modifier_autre_produit_url_resolves(self):
        url = reverse('ProduitApp:modifier_autre_produit', args=[1])
        self.assertEquals(resolve(url).func.view_class, modifier_autre_produit)

    def test_add_autre_produit_url_resolves(self):
        url = reverse('ProduitApp:add_autre_produit')
        self.assertEquals(resolve(url).func, add_autre_produit)

    def test_autre_produit_detail_url_resolves(self):
        url = reverse('ProduitApp:autre_produit_detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, autre_produit_detail)

    def test_supprimer_autre_produit_url_resolves(self):
        url = reverse('ProduitApp:supprimer_autre_produit', args=[1])
        self.assertEquals(resolve(url).func.view_class, supprimer_autre_produit)

    def test_recherche_autre_produit_url_resolves(self):
        url = reverse('ProduitApp:recherche_autre_produit')
        self.assertEquals(resolve(url).func, recherche_autre_produit)

    def test_cadre_url_resolves(self):
        url = reverse('ProduitApp:cadre')
        self.assertEquals(resolve(url).func, cadre)

    def test_create_cadre_url_resolves(self):
        url = reverse('ProduitApp:create_cadre')
        self.assertEquals(resolve(url).func, createCadre)

    def test_supprimer_cadre_url_resolves(self):
        url = reverse('ProduitApp:supprimer_cadre', args=[1])
        self.assertEquals(resolve(url).func, supprimer_cadre)
    def test_modifier_cadre_url_resolves(self):
        url = reverse('ProduitApp:modifier_cadre', args=[1])
        self.assertEquals(resolve(url).func.view_class, modifier_cadre)

    def test_tri_cadre_url_resolves(self):
        url = reverse('ProduitApp:tri_cadre', args=['prix'])
        self.assertEquals(resolve(url).func, tri_cadre)

    def test_produitApp_url_resolves(self):
        url = reverse('ProduitApp:produitApp')
        self.assertEquals(resolve(url).func, index)

    def test_categorie_url_resolves(self):
        url = reverse('ProduitApp:categorie')
        self.assertEquals(resolve(url).func, categorie)

    def test_create_categorie_url_resolves(self):
        url = reverse('ProduitApp:create_categorie')
        self.assertEquals(resolve(url).func, create_category)

    def test_modifier_categorie_url_resolves(self):
        url = reverse('ProduitApp:modifier_categorie', args=[1])
        self.assertEquals(resolve(url).func.view_class, modifier_categorie)

    def test_supprimer_categorie_url_resolves(self):
        url = reverse('ProduitApp:supprimer_categorie', args=[1])
        self.assertEquals(resolve(url).func.view_class, supprimer_categorie)



#test unitaire views.py
class AutreProduitViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.categorie = Categorie.objects.create(name='Catégorie de test')
        self.autre_produit_url = reverse('ProduitApp:autre_produit')

        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=self.categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )


    def test_autre_produit_view(self):
        response = self.client.get(self.autre_produit_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProduitApp/autre_produit.html')
        self.assertContains(response, self.autre_produit.designation)



class CadreViewTestCase(TestCase):
    def setUp(self):

        self.cadre = Cadre.objects.create(cadre_choix='Cadre')
    def test_cadre_view(self):
        response = self.client.get(reverse('ProduitApp:cadre'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProduitApp/cadres.html')
        self.assertContains(response, self.cadre.cadre_choix)


class SupprimerCadreTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.cadre = Cadre.objects.create(cadre_choix="Cadre1")
    def test_supprimer_cadre(self):
        self.cadre.delete()
        self.assertFalse(Cadre.objects.filter(id=self.cadre.id).exists())


class ModifierCadreTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.cadre = Cadre.objects.create(cadre_choix="Cadre1")
        self.data = {'cadre_choix': 'Cadre2'}

    def test_modifier_cadre(self):
        cadre = Cadre.objects.get(id=self.cadre.id)
        self.assertTrue(cadre.cadre_choix, 'Cadre2')



# test unitaire création catégorie
class CreateCategoryTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_create_category(self):
        # Vérifier que la page de création de catégorie est accessible
        response = self.client.get(reverse('ProduitApp:create_categorie'))
        self.assertEqual(response.status_code, 200)

        # Vérifier que la création de catégorie fonctionne
        data = {'name': 'Nouvelle catégorie'}
        response = self.client.post(reverse('ProduitApp:create_categorie'), data=data)
        self.assertEqual(response.status_code, 302)

        # Vérifier que la nouvelle catégorie a bien été créée
        categories = Categorie.objects.all()
        self.assertEqual(len(categories), 1)
        self.assertEqual(categories[0].name, 'Nouvelle catégorie')

class CategorieViewTestCase(TestCase):
    def setUp(self):
        Categorie.objects.create(name='category1')
        Categorie.objects.create(name='category2')
        Categorie.objects.create(name='produit brut')
        Categorie.objects.create(name='cadre')

    def test_categorie_view(self):
        response = self.client.get(reverse('ProduitApp:categorie'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProduitApp/categorie.html')

# test unitaire supprimer catégorie
class SupprimerCategorieTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name='Test')

    def test_get(self):
        response = self.client.get(reverse('ProduitApp:supprimer_categorie', kwargs={'pk': self.categorie.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProduitApp/supprimer_categorie.html')

    def test_post(self):
        data = {'pk': self.categorie.pk}
        response = self.client.post(reverse('ProduitApp:supprimer_categorie', kwargs={'pk': self.categorie.pk}), data=data)
        self.assertRedirects(response, reverse('ProduitApp:categorie'))
        self.assertFalse(Categorie.objects.filter(pk=self.categorie.pk).exists())

# test unitaire modifier catégorie
class TestModifierCategorieView(TestCase):

    def setUp(self):
        self.client = Client()
        self.categorie = Categorie.objects.create(name='Test Category')
        self.url = reverse('ProduitApp:modifier_categorie', args=[self.categorie.id])
        self.data = {
            'name': 'New Test Category'
        }
        self.form = CategorieForm(data=self.data, instance=self.categorie)

    def test_get(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ProduitApp/modifier_categorie.html')
        self.assertIsInstance(response.context['form'], CategorieForm)
        self.assertEqual(response.context['form'].instance, self.categorie)

    def test_post(self):
        response = self.client.post(self.url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('ProduitApp:categorie'))
        self.categorie.refresh_from_db()
        self.assertEqual(self.categorie.name, 'New Test Category')




# test unitaire detail d'autre produit
class AutreProduitDetailTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name='category1')
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=self.categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )
        self.url = reverse('ProduitApp:autre_produit_detail', args=[self.autre_produit.pk])
        self.response = self.client.get(self.url)

    def test_autre_produit_detail_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_autre_produit_detail_view_template(self):
        self.assertTemplateUsed(self.response, 'ProduitApp/autre_produit_detail.html')

    def test_autre_produit_detail_view_contains_autre_produit_details(self):
        self.assertContains(self.response, self.autre_produit.designation)
        self.assertContains(self.response, self.autre_produit.categorie.name)
        self.assertContains(self.response, self.autre_produit.prix_vente)
        self.assertContains(self.response, self.autre_produit.prix_achat)
        self.assertContains(self.response, self.autre_produit.quantite)
        self.assertContains(self.response, self.autre_produit.stock_alerte)

# test unitaire modifier autre produit
class ModifierAutreProduitTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name='category1')
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=self.categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )
        self.url = reverse('ProduitApp:modifier_autre_produit', args=[self.autre_produit.pk])
        self.response = self.client.get(self.url)

    def test_modifier_autre_produit_view_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_modifier_autre_produit_view_template(self):
        self.assertTemplateUsed(self.response, 'ProduitApp/modifier_autre_produit.html')

    def test_modifier_autre_produit_view_contains_form(self):
        form = self.response.context.get('form')
        self.assertIsInstance(form, AutreProduitForm)


# test unitaire supprimer autre produit
class SupprimerAutreProduitTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name='category1')
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=self.categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )
        self.url = reverse('ProduitApp:supprimer_autre_produit', args=[self.autre_produit.pk])
        self.response = self.client.post(self.url)

    def test_autre_produit_is_deleted(self):
        self.assertFalse(AutreProduit.objects.filter(pk=self.autre_produit.pk).exists())

    def test_supprimer_autre_produit_view_status_code(self):
        self.assertEqual(self.response.status_code, 302)

    def test_supprimer_autre_produit_view_redirects_to_autre_produit_list(self):
        self.assertRedirects(self.response, reverse('ProduitApp:autre_produit'))

    def test_autre_produit_list_does_not_contain_deleted_autre_produit(self):
        response = self.client.get(reverse('ProduitApp:autre_produit'))
        self.assertNotContains(response, self.autre_produit.designation)

# test unitaire recherche autre produit
class AutreProduitSearchTestCase(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(name='category1')
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=self.categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )
        self.url = reverse('ProduitApp:recherche_autre_produit')

    def test_recherche_autre_produit_view_status_code(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)

    def test_recherche_autre_produit_view_with_search_query(self):
        response = self.client.get(self.url, {'search_query': 'Test produit'})
        self.assertEqual(response.status_code, 200)

    def test_recherche_autre_produit_view_with_empty_search_query(self):
        response = self.client.get(self.url, {'search_query': ''})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['autre_produit'], [])

    def test_recherche_autre_produit_view_with_nonexistent_search_query(self):
        response = self.client.get(self.url, {'search_query': 'Nonexistent produit'})
        self.assertEqual(response.status_code, 200)
        self.assertQuerysetEqual(response.context['autre_produit'], [])
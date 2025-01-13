from django.test import TestCase
from django.test import TestCase, RequestFactory,SimpleTestCase, Client
from django.urls import reverse,resolve
from decimal import Decimal
from .models import *
from .views import *
from django.test import TestCase
from django.urls import reverse
from django.utils.translation import activate
from django.views.i18n import JavaScriptCatalog
from ProduitApp.models import *
from FournisseursApp.models import *
#Test unitaire pour urls.py
class MyappTestCase(TestCase):
    
    def test_index_url_resolves(self):
        url = reverse('achat')
        self.assertEqual(resolve(url).func, index)
    
    def test_supprimer_achat_url_resolves(self):
        url = reverse('supprimer_achat', args=[1])
        self.assertEqual(resolve(url).func.view_class, AchatDeleteView)
    
    def test_modifier_achat_url_resolves(self):
        url = reverse('modifier_achat', args=[1])
        self.assertEqual(resolve(url).func.view_class, AchatUpdateView)
    
    def test_ajouter_produits_url_resolves(self):
        url = reverse('ajouter_produits')
        self.assertEqual(resolve(url).func, ajouter_produits)
    
    def test_jsi18n_url_resolves(self):
        url = reverse('js-catlog')
        self.assertEqual(resolve(url).func.view_class, JavaScriptCatalog)

    
    

class AchatModelTestCase(TestCase):
    
    def setUp(self):
        self.fournisseur = Fournisseurs.objects.create(Raison_social= 'Fournisseur Test',
            email='test@example.com',
            Numero_Telephone= '+33123456789',
            Versement= 1000,
            Dette= 500,)
        
        categorie = Categorie.objects.create(name='produit brut')

        self.produit_brut = ProduitBrut.objects.create(
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
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )
        
        self.achat = Achat.objects.create(
            fournisseur=self.fournisseur,
            date_achat='2022-04-09 10:00:00',
            prix_total=50.0,
            Versement=20.0,
            Versement_totalite=False,
            Dette=30.0,
            fichier=None
        )
        self.produit_brut_liaison = ProduitBrutLiaison.objects.create(
            achat=self.achat,
            produit_brut=self.produit_brut,
            quantite_quintal=5,
            quantite_metre=5,
            quantite_bar=5,
            prix_total=5,

        )
        self.autre_produit_liaison = AutreProduitLiaison.objects.create(
            achat=self.achat,
            autre_produit=self.autre_produit,
            quantite=3,
            prix_total=2,
        )
       
        self.achat.produits_bruts.add(self.produit_brut)
        self.achat.autre_produits.add(self.autre_produit)
        
    
    def test_fournisseur_field(self):
        field_label = self.achat._meta.get_field('fournisseur').verbose_name
        self.assertEqual(field_label, 'fournisseur')
        self.assertEqual(self.achat.fournisseur, self.fournisseur)
    
    def test_date_achat_field(self):
        field_label = self.achat._meta.get_field('date_achat').verbose_name
        self.assertEqual(field_label, 'date achat')
        self.assertEqual(str(self.achat.date_achat), '2022-04-09 10:00:00')
    
    def test_prix_total_field(self):
        field_label = self.achat._meta.get_field('prix_total').verbose_name
        self.assertEqual(field_label, 'prix total')
        self.assertEqual(self.achat.prix_total, 50.0)
    
    def test_Versement_field(self):
        field_label = self.achat._meta.get_field('Versement').verbose_name
        self.assertEqual(field_label, 'Versement')
        self.assertEqual(self.achat.Versement, 20.0)
    
    def test_Versement_totalite_field(self):
        field_label = self.achat._meta.get_field('Versement_totalite').verbose_name
        self.assertEqual(field_label, 'Versement totalite')
        self.assertFalse(self.achat.Versement_totalite)
    
    def test_fichier_field(self):
        field_label = self.achat._meta.get_field('fichier').verbose_name
        self.assertEqual(field_label, 'fichier')
       
    
    def test_produits_bruts_field(self):
        produits_bruts = self.achat.produits_bruts.all()
        self.assertEqual(len(produits_bruts), 1)
        self.assertEqual(produits_bruts[0], self.produit_brut)
    
    def test_autre_produits_field(self):
        autre_produits = self.achat.autre_produits.all()
        self.assertEqual(len(autre_produits), 1)
        self.assertEqual(autre_produits[0], self.autre_produit)
    
 
    
   
#test unitaire views.py


class IndexViewTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse('achat'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'achat.html')
        self.assertContains(response, 'Liste des achats')
        self.assertQuerysetEqual(response.context['achats'], Achat.objects.all(), transform=lambda x: x)

class AchatDeleteViewTestCase(TestCase):
    def setUp(self):
        self.fournisseur = Fournisseurs.objects.create(Raison_social= 'Fournisseur Test',
            email='test@example.com',
            Numero_Telephone= '+33123456789',
            Versement= 1000,
            Dette= 500,)
        
        categorie = Categorie.objects.create(name='produit brut')

        self.produit_brut = ProduitBrut.objects.create(
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
        self.autre_produit = AutreProduit.objects.create(
            designation='Test produit',
            description='Description de test',
            TVA=20,
            categorie=categorie,
            prix_vente=10.50,
            prix_achat=5.00,
            quantite=10.00,
            stock_alerte=5.00,
        )
        
        self.achat = Achat.objects.create(
            fournisseur=self.fournisseur,
            date_achat='2022-04-09 10:00:00',
            prix_total=50.0,
            Versement=20.0,
            Versement_totalite=False,
            Dette=30.0,
            fichier=None
        )
        self.produit_brut_liaison = ProduitBrutLiaison.objects.create(
            achat=self.achat,
            produit_brut=self.produit_brut,
            quantite_quintal=5,
            quantite_metre=5,
            quantite_bar=5,
            prix_total=5,

        )
        self.autre_produit_liaison = AutreProduitLiaison.objects.create(
            achat=self.achat,
            autre_produit=self.autre_produit,
            quantite=3,
            prix_total=2,
        )
       
        self.achat.produits_bruts.add(self.produit_brut)
        self.achat.autre_produits.add(self.autre_produit)
        

        self.url = reverse('supprimer_achat', kwargs={'pk': self.achat.pk})

    def test_delete_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'supprimer_achat.html')

    def test_delete_view_post(self):
        response = self.client.post(self.url, follow=True)
        self.assertRedirects(response, reverse('achat'))
        self.assertFalse(Achat.objects.filter(pk=self.achat.pk).exists())

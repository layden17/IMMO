
"""
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Commande


from django.test import TestCase, RequestFactory,SimpleTestCase, Client
from django.urls import reverse,resolve
from .models import Commande, Article, ArticleCadre,ArticleAutre,AutreProduit
# Create your tests here.

#test unitaire de urls.py
class TestUrls(TestCase):

    def test_venteApp_url_resolves(self):
        url = reverse('VenteApp:venteApp')
        self.assertEqual(url, '/venteApp/')

    def test_pcreate_url_resolves(self):
        url = reverse('VenteApp:venteApp2')
        self.assertEqual(url, '/venteApp2/')

    def test_proformat_url_resolves(self):
        url = reverse('VenteApp:proformat')
        self.assertEqual(url, '/proformat/')

    def test_updateOrder_url_resolves(self):
        url = reverse('VenteApp:update_order', args=['1'])
        self.assertEqual(url, '/update_order/1/')

    def test_deleteOrder_url_resolves(self):
        url = reverse('VenteApp:delete_order', args=['1'])
        self.assertEqual(url, '/delete_order/1/')

    def test_searchBar_url_resolves(self):
        url = reverse('VenteApp:search')
        self.assertEqual(url, '/recherche/')

    def test_ViewPDF_url_resolves(self):
        url = reverse('VenteApp:pdf_view')
        self.assertEqual(url, '/pdf_view/')

    def test_DownloadPDF_url_resolves(self):
        url = reverse('VenteApp:pdf_download')
        self.assertEqual(url, '/pdf_download/')

    def test_requeteManuel_url_resolves(self):
        url = reverse('VenteApp:requete')
        self.assertEqual(url, '/sql/')

    def test_deleteData_url_resolves(self):
        url = reverse('VenteApp:data')
        self.assertEqual(url, '/data/')

    def test_createCadre_url_resolves(self):
        url = reverse('VenteApp:cadre')
        self.assertEqual(url, '/order/create/cadre')

    def test_pos_url_resolves(self):
        url = reverse('VenteApp:pos')
        self.assertEqual(url, '/pos/')

    def test_checkout_modal_url_resolves(self):
        url = reverse('VenteApp:checkout-modal')
        self.assertEqual(url, '/checkout-modal')

    def test_save_pos_url_resolves(self):
        url = reverse('VenteApp:save-pos')
        self.assertEqual(url, '/save-pos')

    def test_receipt_url_resolves(self):
        url = reverse('VenteApp:receipt-modal')
        self.assertEqual(url, '/receipt')

    def test_OrderDetail_url_resolves(self):
        url = reverse('VenteApp:order_details', args=['1'])
        self.assertEqual(url, '/orders/1')

    def test_commandes_client_url_resolves(self):
        url = reverse('VenteApp:commandes')
        self.assertEqual(url, '/orders/client/commandes')

    def test_OrderCreate_url_resolves(self):
        url = reverse('VenteApp:order_create')
        self.assertEqual(url, '/order/create/')

    def test_OrderList_url_resolves(self):
        url = reverse('VenteApp:orders')
        self.assertEqual(url, '/orders/')

    def test_total_qty_url_resolves(self):
        url = reverse('VenteApp:total_qty', args=['1'])
        self.assertEqual(url, '/1/total_qty/')

    def test_commandes_client_url_resolves(self):
        url = reverse('VenteApp:commandes', args=['1'])
        self.assertEqual(url, '/customer/1/orders/')



||||||| .r167
# Create your tests here.
=======


from VenteApp.models import Commande,Article,ArticleAutre,ArticleCadre
from VenteApp.forms import VenteForms, ArticleForms, ArticleCadreForms,ArticleAutreForms
from ProduitApp.models import Produit,ProduitBrut,AutreProduit,Cadre,Categorie
from ClientApp.models import Client

class IndexViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.url = reverse('venteApp')
        categorie = Categorie.objects.create(name='test')

        self.produit = Produit.objects.create(
            designation = 'produit_test',
            description ='test',
            TVA= 0,
            categorie= categorie,
            stock_alerte=0

            )
        self.client = Client.objects.create(
            nom='client_test',
            email='client_test@test.com',
            prenom = 'p_client_test',
            type ='Particulier',
            adresse ='adresse_test',
            tel = '01234567',
            dette = 0
            )
        
        self.commande = Commande.objects.create(client=self.client)
        
    def test_index_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'VenteApp/index.html')
        self.assertEqual(response.context['product'], 1)
        self.assertEqual(response.context['customer'], 1)
        self.assertEqual(response.context['order'], 1)
        self.assertContains(response, 'produit_test')
        self.assertContains(response, 'client_test')




class TestUrls(TestCase):

    def setUp(self):
        self.order = Commande.objects.create(
            customer="John Doe",
            date_ordered=timezone.now(),
            complete=False
        )

    def test_venteApp_url_resolves(self):
        url = reverse('venteApp')
        self.assertEqual(url, '/vente/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_order_url_resolves(self):
        url = reverse('update_order', args=[self.order.id])
        self.assertEqual(url, f'/update_order/{self.order.id}/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_delete_order_url_resolves(self):
        url = reverse('delete_order', args=[self.order.id])
        self.assertEqual(url, f'/delete_order/{self.order.id}/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_searchBar_url_resolves(self):
        url = reverse('search')
        self.assertEqual(url, '/recherche/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pdf_view_url_resolves(self):
        url = reverse('pdf_view')
        self.assertEqual(url, '/pdf_view/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_pdf_download_url_resolves(self):
        url = reverse('pdf_download')
        self.assertEqual(url, '/pdf_download/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_createCadre_url_resolves(self):
        url = reverse('cadre')
        self.assertEqual(url, '/order/create/cadre')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_order_details_url_resolves(self):
        url = reverse('order_details', args=[self.order.id])
        self.assertEqual(url, f'/orders/{self.order.id}')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_commandes_client_url_resolves(self):
        url = reverse('commandes_client')
        self.assertEqual(url, '/orders/client/commandes')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_order_create_url_resolves(self):
        url = reverse('order_create')
        self.assertEqual(url, '/order/create/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_orders_url_resolves(self):
        url = reverse('orders')
        self.assertEqual(url, '/orders/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_total_qty_url_resolves(self):
        url = reverse('total_qty', args=[self.order.id])
        self.assertEqual(url, f'/{self.order.id}/total_qty/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_commandes_client_url_resolves(self):
        url = reverse('commandes_client', args=[self.client.id])
        self.assertEqual(url, f'/customer/{self.client.id}/orders/')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
















class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_vente = reverse('venteApp')
        self.url_create_order = reverse('order_create')
        self.url_commandes_client = reverse('commandes_client', args=[1]) # 1 étant un ID client existant dans la base de données
        self.url_total_qty = reverse('total_qty', args=[1]) # 1 étant un ID commande existant dans la base de données
        self.order = Commande.objects.create(
            client=Client.objects.create(
                prenom='John',
                nom='Doe',
                email='john.doe@example.com',
                type='Particulier',
                adresse='123 rue des exemples',
                tel='0123456789',
                dette=0
            )
        )
        self.product = Produit.objects.create(
            nom='Test Product',
            description='Ceci est un produit de test',
            prix_vente=10
        )

    def test_index_view(self):
        response = self.client.get(self.url_vente)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/index.html')

    def test_create_order_view(self):
        response = self.client.get(self.url_create_order)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/order_form.html')
        form = response.context['form']
        self.assertIsInstance(form, VenteForms)

        data = {
            'client': self.order.client.id,
            'produit': self.product.id,
            'quantite': 2,
            'prix_unite': self.product.prix_vente
        }
        response = self.client.post(self.url_create_order, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Commande.objects.count(), 2)

    def test_commandes_client_view(self):
        response = self.client.get(self.url_commandes_client)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/commandes_client.html')
        orders = response.context['orders']
        self.assertQuerysetEqual(orders, [repr(self.order)], transform=repr)

    def test_total_qty_view(self):
        response = self.client.get(self.url_total_qty)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/total_qty.html')
        self.assertContains(response, 'Total quantité : 0')
        self.order.articles_produits.create(
            produit=self.product,
            quantite=2,
            prix_unite=self.product.prix_vente
        )
        response = self.client.get(self.url_total_qty)
        self.assertContains(response, 'Total quantité : 2')









class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.url_vente = reverse('venteApp')
        self.url_create_order = reverse('order_create')
        self.url_commandes_client = reverse('commandes_client', args=[1]) # 1 étant un ID client existant dans la base de données
        self.url_total_qty = reverse('total_qty', args=[1]) # 1 étant un ID commande existant dans la base de données
        self.order = Commande.objects.create(
            client=Client.objects.create(
                prenom='John',
                nom='Doe',
                email='john.doe@example.com',
                type='Particulier',
                adresse='123 rue des exemples',
                tel='0123456789',
                dette=0
            )
        )
        self.product = Produit.objects.create(
            nom='Test Product',
            description='Ceci est un produit de test',
            prix_vente=10
        )

    def test_index_view(self):
        response = self.client.get(self.url_vente)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/index.html')

    def test_create_order_view(self):
        response = self.client.get(self.url_create_order)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/order_form.html')
        form = response.context['form']
        self.assertIsInstance(form, VenteForms)

        data = {
            'client': self.order.client.id,
            'produit': self.product.id,
            'quantite': 2,
            'prix_unite': self.product.prix_vente
        }
        response = self.client.post(self.url_create_order, data=data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Commande.objects.count(), 2)

    def test_commandes_client_view(self):
        response = self.client.get(self.url_commandes_client)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/commandes_client.html')
        orders = response.context['orders']
        self.assertQuerysetEqual(orders, [repr(self.order)], transform=repr)

    def test_total_qty_view(self):
        response = self.client.get(self.url_total_qty)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'venteApp/total_qty.html')
        self.assertContains(response, 'Total quantité : 0')
        self.order.articles_produits.create(
            produit=self.product,
            quantite=2,
            prix_unite=self.product.prix_vente
        )
        response = self.client.get(self.url_total_qty)
        self.assertContains(response, 'Total quantité : 2')








class ArticleAutreTestCase(TestCase):
    
    def setUp(self):
        self.commande = Commande.objects.create(client="John Doe")
        self.produit = AutreProduit.objects.create(nom="Crayon", prix_vente=1.5)
        self.article = ArticleAutre.objects.create(commande=self.commande, produit=self.produit, quantite=2)
    
    def test_price(self):
        self.assertEqual(self.article.price, 3.0)
    
    def test_string_representation(self):
        self.assertEqual(str(self.article), "2 x Crayon")
    
    def test_save(self):
        self.assertEqual(self.article.prix_unite, 1.5)













class ArticleModelTest(TestCase):

    def setUp(self):
        self.commande = Commande.objects.create(numero_commande='123456')
        self.produit_brut = ProduitBrut.objects.create(nom='Produit test', prix_barre=10, prix_metre=20, prix_quintal=30)
        self.article = Article.objects.create(commande=self.commande, produit=self.produit_brut, unite='Par barre', quantite=3)

    def test_price(self):
        expected_price = 30 # 3 barres x 10€ par barre
        self.assertEqual(self.article.price, expected_price)

    def test_str(self):
        expected_str = '3 x Produit test'
        self.assertEqual(str(self.article), expected_str)









class CommandeTest(TestCase):
    def setUp(self):
        self.client1 = Client.objects.create(nom='John', prenom='Doe', email='john@example.com')
        self.commande1 = Commande.objects.create(client=self.client1, statut='En attente', remise=10)
        self.commande2 = Commande.objects.create(client=self.client1, statut='Livré', remise=20)

    def test_commande_est_creee(self):
        self.assertEqual(self.commande1.statut, 'En attente')
        self.assertEqual(self.commande1.remise, 10)
        self.assertIsNotNone(self.commande1.date_creation)

    def test_commande_str(self):
        self.assertEqual(str(self.commande1), f"Commande #{self.commande1.id} - {self.commande1.client.nom} {self.commande1.client.prenom}")

    def test_commande_date_reception(self):
        self.assertIsNone(self.commande1.date_reception)
        self.commande1.date_reception = timezone.now()
        self.commande1.save()
        self.assertIsNotNone(self.commande1.date_reception)

    def test_calcul_taxes(self):
        self.commande1.tendered_amount = 100
        self.commande1.amount_change = 0
        self.commande1.save()
        self.assertEqual(self.commande1.tax_amount, 0)
        self.assertEqual(self.commande1.tax, 0)
        self.commande2.tendered_amount = 100
        self.commande2.amount_change = 0
        self.commande2.save()
        self.assertEqual(self.commande2.tax_amount, 20)
        self.assertEqual(self.commande2.tax, 0.2)
"""
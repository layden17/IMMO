from django.test import TestCase

# Create your tests here.

from .models import Cadre, ProduitBrut

class CadreTest(TestCase):
    def setUp(self):
        self.cadre1 = Cadre.objects.create(
            cadre_choix='Cadre',
            prix_metre=10.0,
            longueur=10.0,
            largeur=5.0,
            crochet=2.0,
            prix_service=5.0,
            chute=False,
            consommation_sans_chute=100.0,
            consommation=100.0,
            crochet_opti=2.0,
            chute_valeur=0.0,
            max=10.0,
            prix=200.0,
        )
        self.produit1 = ProduitBrut.objects.create(
            nom='produit1',
            prix_unitaire=5.0,
            quantite_stock=100,
        )
        self.cadre1.article_choix.add(self.produit1)

    def test_cadre_creation(self):
        self.assertEqual(self.cadre1.cadre_choix, 'Cadre')
        self.assertEqual(self.cadre1.prix_metre, 10.0)
        self.assertEqual(self.cadre1.longueur, 10.0)
        self.assertEqual(self.cadre1.largeur, 5.0)
        self.assertEqual(self.cadre1.crochet, 2.0)
        self.assertEqual(self.cadre1.prix_service, 5.0)
        self.assertFalse(self.cadre1.chute)
        self.assertEqual(self.cadre1.consommation_sans_chute, 100.0)
        self.assertEqual(self.cadre1.consommation, 100.0)
        self.assertEqual(self.cadre1.crochet_opti, 2.0)
        self.assertEqual(self.cadre1.chute_valeur, 0.0)
        self.assertEqual(self.cadre1.max, 10.0)
        self.assertEqual(self.cadre1.prix, 200.0)

    def test_cadre_article_choix(self):
        self.assertEqual(self.cadre1.article_choix.first(), self.produit1)
        self.assertEqual(self.cadre1.article_choix.count(), 1)

    def test_cadre_prix_total(self):
        self.assertEqual(self.cadre1.prix(), 250.0)

from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView
from django.template import loader

from .forms import ProduitBrutForm, CadreForms, AutreProduitForm


# Create your views here.

from django.contrib import messages
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse
from .models import ProduitBrut, Produit, Categorie, Cadre, AutreProduit, CategorieFer
from .forms import CategorieForm, CadreForms


def get_categorie_data(request):
    name = request.GET.get('name', '')
    categorie = CategorieFer.objects.get(name=name)
    data = {
        'nb_m_par_quintal': categorie.nb_m_par_quintal,
        'nb_bar_par_quintal': categorie.nb_bar_par_quintal,
    }
    return JsonResponse(data)




def index(request):
    return render(request, 'ProduitApp/produit_base.html')


"""
view pour afficher les autres produits 
"""
def autre_produit(request):
    autre_produit = AutreProduit.objects.all()
    return render(request, 'ProduitApp/autre_produit.html',
                            {'autres_produits': autre_produit})




"""
view pour afficher les produits brut (barre de fer)
"""
def produit_brut(request):
    produits_bruts = ProduitBrut.objects.all()
    return render(request, 'ProduitApp/produits_bruts.html',
                            {'produits_bruts': produits_bruts})

"""
view pour afficher les cadres 
"""
def cadre(request):
    cadres = Cadre.objects.all()

    #cadres = Produit.objects.filter(categorie__name='cadre')
    return render(request, 'ProduitApp/cadres.html', {'cadres': cadres})



def createCadre(request):
    form = CadreForms()
    if request.method == 'POST':
        form= CadreForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/cadre/')
    return render(request, 'ProduitApp/create_cadre.html', {'form': form})


"""
def createCadre(request):
    if request.method == 'POST':
        shape = request.POST['cadre_choix']
        article = request.POST['article_choix']
        length = request.POST['longueur']
        width = request.POST['largeur']
        hook = request.POST['crochet']
        service_price = request.POST['prix_service']

        form = CadreForms(shape=shape, article=article, length=length, width=width, hook=hook, service_price=service_price)
        form.save()

        return redirect('/cadre/')

    return render(request, 'ProduitApp/create_cadre.html')

"""


def supprimer_cadre(request, id):
    cadre = Cadre.objects.get(id=id)
    cadre.delete()
    return redirect('/cadre/')



class modifier_cadre(UpdateView):
    model = Cadre
    form_class = CadreForms
    template_name = 'ProduitApp/modifier_cadre.html'
    def form_valid(self, form):
        form.save()
        return redirect('/cadre/')

def tri_cadre(request, tri):
    if tri == 'Cadre_choix':
        cadre = Cadre.objects.order_by('cadre_choix')
    elif tri == 'Article_choix':
        cadre = Cadre.objects.order_by('article_choix')
    elif tri == 'longueur':
        cadre = Cadre.objects.order_by('longueur')
    elif tri == 'largeur':
        cadre = Cadre.objects.order_by('largeur')
    elif tri == 'crochet':
        cadre = Cadre.objects.order_by('crochet')
    elif tri == 'prix_service':
        cadre = Cadre.objects.order_by('prix_service')
    elif tri == 'chute':
        cadre = Cadre.objects.order_by('chute')
    elif tri == 'prix':
        cadre = Cadre.objects.order_by('prix')
    else:
        cadre = Cadre.objects.all()
    return render(request, 'ProduitApp/cadres.html', {'cadres': cadre})






def create_category(request):
    form = CategorieForm
    if request.method == 'POST':
        form = CategorieForm(request.POST)
        if form.is_valid():
            categorie = Categorie(name=form.cleaned_data['name'])
            categorie.save()
            return HttpResponseRedirect('/produit_brut/')
    else:
        form = CategorieForm
    return render(request, 'ProduitApp/create_categorie.html', {'form': form})



def add_produit_brut(request):
    form = ProduitBrutForm()
    if request.method == 'POST':
        form = ProduitBrutForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/produit_brut/')
    else:
        form = ProduitBrutForm()

    context = {'form': form}
    return render(request, 'ProduitApp/add_produit_brut.html', context)


def add_autre_produit(request):
    form = AutreProduitForm()
    if request.method == 'POST':
        form = AutreProduitForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/autre_produit/')
    else:
        form = AutreProduitForm()

    context = {'form': form}
    return render(request, 'ProduitApp/add_autre_produit.html', context)


class produit_detail(DetailView):
    model = ProduitBrut
    template_name = 'ProduitApp/produit_detail.html'


class autre_produit_detail(DetailView):
    model = AutreProduit
    template_name = 'ProduitApp/autre_produit_detail.html'


class modifier_produit(UpdateView):
    model = ProduitBrut
    form_class = ProduitBrutForm
    template_name = 'ProduitApp/modifier_produit.html'

    def get_success_url(self) :
        return reverse_lazy("ProduitApp:produit_detail",kwargs={'pk':self.object.id})

class modifier_autre_produit(UpdateView):
    model = AutreProduit
    form_class = AutreProduitForm
    template_name = 'ProduitApp/modifier_autre_produit.html'

    def get_success_url(self) :
        return reverse_lazy("ProduitApp:autre_produit_detail",kwargs={'pk':self.object.id})



class supprimer_produit_brut(DeleteView):
    model=ProduitBrut
    template_name='ProduitApp/supprimer_produit_brut.html'
    success_url = reverse_lazy('ProduitApp:produit_brut')



class supprimer_autre_produit(DeleteView):
    model=AutreProduit
    template_name='ProduitApp/supprimer_autre_produit.html'
    success_url = reverse_lazy('ProduitApp:autre_produit')




"""
class modifier_produit(UpdateView):
    model = ProduitBrut
    form_class = ProduitBrutForm
    template_name = 'modifier_produit.html'
    success_url = reverse_lazy('ProduitApp/add_produit_brut.html')


def modifier_produit(request, produit_id):
    produit = get_object_or_404(Produit, pk=produit_id)
    if request.method == 'POST':
        form = ProduitBrutForm(request.POST, instance=produit)
        if form.is_valid():
            form.save()
            return redirect('/produit_brut/')
    else:
        form = ProduitBrutForm(instance=produit)
    return render(request, 'ProduitApp/modifier_produit.html', {'form': form})
"""

from django.shortcuts import render, redirect

from .models import Fournisseurs
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Fournisseurs
from .forms import FournisseurForm
# Create your views here.



def index(request):
    # Récupère tous les fournisseurs et les passe au template 'fournisseurs.html' pour les afficher
    return render(request, "fournisseurs.html", {'fournisseurs': Fournisseurs.objects.all()})

def ajout_fournisseurs(request):
    # Vérifie si la méthode HTTP utilisée est POST
    if request.method == 'POST':
        # Crée une instance de FournisseurForm avec les données POST et les fichiers téléchargés
        fournisseur_form = FournisseurForm(request.POST, request.FILES)
        # Vérifie si le formulaire est valide
        if fournisseur_form.is_valid():
            # Enregistre le formulaire et crée une nouvelle instance de FournisseurForm
            fournisseur_form.save()
            fournisseur_form.clean()
            fournisseur_form = FournisseurForm()
    else:
        # Crée une nouvelle instance de FournisseurForm
        fournisseur_form = FournisseurForm()
    # Passe l'instance de FournisseurForm au template 'ajout_fournisseurs.html' pour l'afficher
    return render(request, 'ajout_fournisseurs.html', {'fournisseur_form': fournisseur_form})






from django.views.generic import DeleteView
from django.urls import reverse_lazy


class FournisseurDeleteView(DeleteView):
    model = Fournisseurs
    template_name = 'supprimer_fournisseurs.html'
    success_url = reverse_lazy('FournisseursApp:fournisseurs')

    def get_context_data(self, **kwargs):
        # Récupère l'objet Fournisseurs à supprimer et le passe au template 'supprimer_fournisseurs.html' pour l'afficher
        context = super().get_context_data(**kwargs)
        context['Fournisseur'] = self.object
        return context


from django.views.generic.edit import UpdateView


class FournisseurUpdateView(UpdateView):
    model = Fournisseurs
    form_class = FournisseurForm
    template_name = 'modifier_fournisseur.html'
    
    def get_success_url(self):
        # Retourne l'URL 'fournisseurs' lorsqu'une mise à jour de fournisseur a réussi
        return reverse_lazy('FournisseursApp:fournisseurs')



from django.shortcuts import render
from django.db.models import Q
from .models import Fournisseurs

def search_fournisseurs(request):
    # Récupère la requête de recherche GET
    query = request.GET.get('search_query')
    # Effectue une recherche en utilisant les termes de recherche dans les champs 'id' et 'Raison_social'
    fournisseurs = Fournisseurs.objects.filter(Q(id__icontains=query) | Q(Raison_social__icontains=query))
    # Passe les résultats de recherche au template 'fournisseurs.html' pour les afficher
    context = {'fournisseurs': fournisseurs}
    return render(request, 'fournisseurs.html', context)


def tri_fournisseurs(request, tri):
    # Vérifie l'argument 'tri' passé dans l'URL pour trier les fournisseurs en conséquence
    if tri == 'id':
        fournisseurs = Fournisseurs.objects.order_by('id')
    elif tri == 'Raison_social':
        fournisseurs = Fournisseurs.objects.order_by('Raison_social')
    elif tri == 'email':
        fournisseurs = Fournisseurs.objects.order_by('email')
    elif tri == 'Numero_Telephone':
        fournisseurs = Fournisseurs.objects.order_by('Numero_Telephone')
    elif tri == 'Fax':
        fournisseurs = Fournisseurs.objects.order_by('Fax')
    elif tri == 'Versement':
        fournisseurs = Fournisseurs.objects.order_by('Versement')
    elif tri == 'Dette':
        fournisseurs = Fournisseurs.objects.order_by('Dette')
    elif tri == 'Facture':
        fournisseurs = Fournisseurs.objects.order_by('Facture')
    else:
        fournisseurs = Fournisseurs.objects.all()
    # Renvoie le résultat trié sous forme d'un dictionnaire contenant la clé 'fournisseurs'
    # pour que le template 'fournisseurs.html' puisse l'afficher
    return render(request, 'fournisseurs.html', {'fournisseurs': fournisseurs})


"""def facture_ajout(request, pk):
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    if request.method == 'POST':
        form = FactureForm(request.POST, request.FILES)
        if form.is_valid():
            facture = form.save(commit=False)
            facture.fournisseur = fournisseur
            facture.save()
            facture.clean()
            facture=FactureForm()
            
    else:
        form = FactureForm()
    return render(request, 'facture_ajout.html', {'form': form, 'fournisseur': fournisseur})"""

from AchatApp.models import Facture

def factures_detail(request, pk):
    # Récupère le fournisseur correspondant à l'ID passé en paramètre
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    # Récupère toutes les factures associées au fournisseur triées par ordre décroissant de date de création
    factures = Facture.objects.filter(fournisseur=fournisseur).order_by('-date_creation')
    # Renvoie le résultat sous forme d'un dictionnaire contenant la clé 'fournisseur' pour afficher
    # les informations du fournisseur dans le template 'factures_detail.html', la clé 'factures'
    # pour afficher la liste des factures, et la clé 'fournisseurs' pour afficher la liste de tous
    # les fournisseurs dans la barre de navigation
    return render(request, 'factures_detail.html', {'fournisseur': fournisseur, 'factures': factures, 'fournisseurs': Fournisseurs.objects.all()})

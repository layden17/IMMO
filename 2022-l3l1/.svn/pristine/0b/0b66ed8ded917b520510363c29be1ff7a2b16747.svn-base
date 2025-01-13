from django.shortcuts import render
from django.shortcuts import render
from .models import Fournisseurs
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Fournisseurs
from .forms import FournisseurForm
# Create your views here.



def index(request):
    return render(request,"fournisseurs.html",{'fournisseurs':Fournisseurs.objects.all()})# Create your views here.

from django.shortcuts import render, redirect


from django.shortcuts import render, redirect
from .forms import FournisseurForm

def ajout_fournisseurs(request):
    if request.method == 'POST':
        fournisseur_form = FournisseurForm(request.POST,request.FILES)
        if fournisseur_form.is_valid():
            fournisseur_form.save()
            fournisseur_form.clean()
            fournisseur_form = FournisseurForm()
    else:
        fournisseur_form = FournisseurForm()
    return render(request, 'ajout_fournisseurs.html', {'fournisseur_form': fournisseur_form})





from django.views.generic import DeleteView
from django.urls import reverse_lazy


class FournisseurDeleteView(DeleteView):
    model = Fournisseurs
    template_name = 'supprimer_fournisseurs.html'
    success_url = reverse_lazy('FournisseursApp:fournisseurs')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Fournisseur'] = self.object
        return context
from django.views.generic.edit import UpdateView


class FournisseurUpdateView(UpdateView):
    model = Fournisseurs
    form_class = FournisseurForm
    template_name = 'modifier_fournisseur.html'
    
    def get_success_url(self):
        return reverse_lazy('FournisseursApp:fournisseurs')


from django.shortcuts import render
from django.db.models import Q
from .models import Fournisseurs

def search_fournisseurs(request):
    query = request.GET.get('search_query')
    fournisseurs = Fournisseurs.objects.filter(Q(id__icontains=query) | Q(Raison_social__icontains=query))
    context = {'fournisseurs': fournisseurs}
    return render(request, 'fournisseurs.html', context)

def tri_fournisseurs(request, tri):
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
   
    fournisseur = get_object_or_404(Fournisseurs, pk=pk)
    factures = Facture.objects.filter(fournisseur=fournisseur).order_by('-date_creation')
    return render(request, 'factures_detail.html', {'fournisseur': fournisseur, 'factures': factures,'fournisseurs':Fournisseurs.objects.all()})

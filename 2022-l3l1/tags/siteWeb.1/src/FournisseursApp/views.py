from django.shortcuts import render
from django.shortcuts import render
from .models import Fournisseurs
from .forms import FournisseurForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404, redirect
from .models import Fournisseurs
# Create your views here.



def index(request):
    return render(request,"fournisseurs.html",{'fournisseurs':Fournisseurs.objects.all()})# Create your views here.

def ajout_fournisseurs(request):
    form=FournisseurForm()
   
    if request.method == 'POST':
        form = FournisseurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form=FournisseurForm()
            messages.success(request, 'Le fournisseur a été ajouté avec succès.')
    
    
    context = { 'form': form}
    

    return render(request,"ajout_fournisseurs.html",context)


from django.views.generic import DeleteView
from django.urls import reverse_lazy
from FournisseursApp.models import Fournisseurs

class FournisseurDeleteView(DeleteView):
    model = Fournisseurs
    template_name = 'supprimer_fournisseurs.html'
    success_url = reverse_lazy('FournisseursApp:fournisseurs')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Fournisseur'] = self.object
        return context
from django.views.generic.edit import UpdateView
from .models import Fournisseurs

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

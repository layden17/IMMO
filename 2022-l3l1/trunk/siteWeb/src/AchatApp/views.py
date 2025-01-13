from django.shortcuts import render
from .models import Achat
from .forms import AchatForm,FactureForm
from django.contrib import messages
# Create your views here.
def index(request):

    return render(request,"achat.html",{"achats":Achat.objects.all()})


from django.shortcuts import render, redirect, get_object_or_404
from FournisseursApp.models import Fournisseurs
from .forms import FactureForm

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Achat, Facture
from .forms import AchatForm, FactureForm

def ajout_achat(request):
    if request.method == 'POST':
        form = AchatForm(request.POST,request.FILES)

        if form.is_valid():
            achat = form.save(commit=False)
            achat.save()
            form.save_m2m()
            form=AchatForm()
            messages.success(request, "L'achat a été ajouté avec succès!")
            return redirect('achat')  # rediriger vers la vue d'ajout de facture pour le fournisseur sélectionné
    else:
        form = AchatForm()
    return render(request, 'ajout_achat.html', {'form': form})

def ajouter_facture(request, fournisseur_id, achat_id):
    fournisseur = Fournisseurs.objects.get(id=fournisseur_id)
    achat = Achat.objects.get(id=achat_id)

    if request.method == 'POST':
        form = FactureForm(request.POST, request.FILES)
        if form.is_valid():
            facture = form.save(commit=False)
            facture.fournisseur = fournisseur
            facture.achat = achat
            facture.save()
            messages.success(request, "La facture a été ajoutée avec succès!")
            return redirect('achat')
    else:
        form = FactureForm()
    return render(request, 'ajout_facture.html', {'form': form, 'fournisseur': fournisseur, 'achat': achat})

from django.views.generic import DeleteView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView


class AchatDeleteView(DeleteView):
    model = Achat
    success_url = reverse_lazy('achat')
    template_name = 'supprimer_achat.html'

class AchatUpdateView(UpdateView):
    model = Achat
    form_class = AchatForm
    template_name = 'modifier_achat.html'
    success_url = reverse_lazy('achat')
# views.py

from django.shortcuts import render
from .models import Produit

from django.shortcuts import render, redirect
from .models import Produit

def ajouter_produits(request):
    produits = Produit.objects.all()

    # Récupérer les produits sélectionnés depuis la session
    produits_selectionnes_ids = request.session.get('produits_selectionnes_ids', [])
    produits_selectionnes = Produit.objects.filter(id__in=produits_selectionnes_ids)

    if request.method == 'POST':
        produit_id = request.POST.get('produit')
        if produit_id:
            # Ajouter le produit sélectionné dans la session
            produits_selectionnes_ids.append(int(produit_id))
            request.session['produits_selectionnes_ids'] = produits_selectionnes_ids

            # Rafraîchir la liste des produits sélectionnés depuis la session
            produits_selectionnes = Produit.objects.filter(id__in=produits_selectionnes_ids)
        elif 'supprimer_produit' in request.POST:
            produit_id = int(request.POST.get('produit_id'))
            produits_selectionnes_ids.remove(produit_id)
            request.session['produits_selectionnes_ids'] = produits_selectionnes_ids

            # Rafraîchir la liste des produits sélectionnés depuis la session
            produits_selectionnes = Produit.objects.filter(id__in=produits_selectionnes_ids)

    context = {
        'produits': produits,
        'produits_selectionnes': produits_selectionnes,
    }
    return render(request, 'ajouter_produits.html', context)

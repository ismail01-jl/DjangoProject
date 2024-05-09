from django.contrib import admin
from .models import Categorie, produit, Fournisseur, ProduitNC , Commande

admin.site.register(Categorie)
admin.site.register(produit)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
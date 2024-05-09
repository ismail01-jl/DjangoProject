from django.shortcuts import render , redirect , get_object_or_404
from django.template import loader
from .models import produit , Categorie
from .forms import ProduitForm
from django.http import HttpResponse
from django.http import HttpResponseRedirect
#AUth
from .forms import UserRegistrationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
#API
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer
from .serializers import ProduitSerializer
from rest_framework import viewsets

class ProductViewset(viewsets.ReadOnlyModelViewSet):
 serializer_class = ProduitSerializer
 def get_queryset(self):
    queryset = produit.objects.filter()
    category_id = self.request.GET.get('category_id')
    if category_id:
        queryset = queryset.filter(Categorie_id=category_id)
    return queryset

class CategoryAPIView(APIView):
    def get(self, request, format=None):
        # Récupérer toutes les catégories en utilisant l'ORM de Django
        categories = Categorie.objects.all()
        # Sérialiser les données à l'aide de notre sérialiseur
        serializer = CategorySerializer(categories, many=True)
        # Renvoyer une réponse contenant les données sérialisées
        return Response(serializer.data)
class ProduitAPIView(APIView):
    def get(self, request):
        produits = produit.objects.all()
        serializer = ProduitSerializer(produits, many=True)
        return Response(serializer.data)
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('acceuil')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})


def index(request):
    return render(request, 'magasin/index.html')
    # Affichage de la page d'accueil du site avec une liste des produits enregistrés dans la base de données
def vetrin(request):
    list=produit.objects.all()
    return render(request,'magasin/vetrin.html',{'list':list})

def catalogue(request):
    produits = produit.objects.all()
    Categories = Categorie.objects.all()

    # Filtrage par catégorie
    categorie = request.GET.get('categorie')
    if categorie:
        produits = produits.filter(Categorie__name=categorie)
        
    # Recherche
    query = request.GET.get('search')
    if query:
        produits = produits.filter(libelle__icontains=query)
    return render(request, 'magasin/catalogue.html', {'produits': produits})
    
def addproduit(request):
    if request.method == "POST" : 
        form = ProduitForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/magasin/catalogue.html')
    else :
        form = ProduitForm()
    return render(request,'magasin/majProduits.html',{'form':form})

def modifier_produit(request, produit_id):
    Produit = get_object_or_404(produit, id=produit_id)
    
    if request.method == 'POST':
        # Créer une instance du formulaire avec les données du produit à modifier
        form = ProduitForm(request.POST, instance=Produit)
        if form.is_valid():
            form.save()
            return redirect('/magasin/catalogue')
    else:
        form = ProduitForm(instance=Produit)
    
    return render(request, 'magasin/modifier_produit.html', {'form': form})

def supprimer_produit(request, produit_id):
    # Récupérer le produit à supprimer en fonction de son ID
    Produit = get_object_or_404(produit, id=produit_id)
    
    if request.method == 'POST':
        Produit.delete()
        return redirect('/magasin/catalogue')
    
    return render(request, 'magasin/supprimer_produit.html', {'produit': Produit})
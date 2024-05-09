# magasin/urls.py
from django.urls import path
from . import views
from .views import CategoryAPIView
from .views import ProduitAPIView
from django.conf import settings
from django.conf.urls.static import static
#from .views import AccueilView
app_name = 'magasin'

urlpatterns = [
    path('addproduit/', views.addproduit, name='addproduit'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('vetrin/', views.vetrin, name='vetrin'),
    #path('magasin/', views.index, name='index'),
    path('modifier/<int:produit_id>/', views.modifier_produit, name='modifier_produit'),
    path('supprimer/<int:produit_id>/', views.supprimer_produit, name='supprimer_produit'),
    path('', views.index, name='index'),
    path('register/',views.register, name = 'register'),
    path('api/category/', CategoryAPIView.as_view()),
    path('api/produit/', ProduitAPIView.as_view())
]

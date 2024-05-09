from django import forms
from .models import produit
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email')

class ProduitForm(forms.ModelForm):
    class Meta:
        model = produit
        fields = ['libelle', 'description', 'prix' , 'image' , 'type' , 'Categorie', 'Fournisseur' ]  
class SupprimerProduitForm(forms.Form):
    confirmation = forms.BooleanField(label='Je confirme la suppression de ce produit', required=True)

from rest_framework.serializers import ModelSerializer
from .models import Categorie
from .models import produit

class CategorySerializer(ModelSerializer):
 class Meta:
    model = Categorie
    fields = ['id', 'name']
class ProduitSerializer(ModelSerializer):
    class Meta:
        model = produit
        fields = '__all__'
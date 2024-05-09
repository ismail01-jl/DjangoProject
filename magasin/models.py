from django.db import models
from datetime import date

class Fournisseur(models.Model):
    nom = models.CharField(max_length=100)
    adresse = models.TextField()
    email = models.EmailField()
    telephone = models.CharField(max_length=8)
    def __str__(self):
        return self.nom + " ("+self.telephone+")"  
class Categorie(models.Model):
    TYPE_CHOICES = [
        ('Al', 'Alimentaire'),
        ('Mb', 'Meuble'),
        ('Sn', 'Sanitaire'),
        ('Vs', 'Vaisselle'),
        ('Vt', 'Vêtement'),
        ('Jx', 'Jouets'),
        ('Ec', 'Electroménager'),
        ('Hm', 'Immeuble'),
        ('Fa', 'Frais'),
        ('Fr', 'Fruits'),
        ('Ta', 'Tapis'),
        ('Lg', 'Linge de Maison'),
        ('Bj', 'Bijoux'),
        ('Dc', 'Décor'),
    ]

    name = models.CharField(max_length=50, default='Alimentaire', choices=TYPE_CHOICES)

    def __str__(self):
        return self.name
        
class produit(models.Model):
    libelle=models.CharField(max_length=100)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3)
    image=models.ImageField(blank=True)
    TYPECHOICES=[('em','emballe'),('fr','frais'),('cs','conserve')]
    type=models.CharField(max_length=2 ,choices=TYPECHOICES,default='em')
    Categorie= models.ForeignKey(Categorie, on_delete=models.CASCADE, null=True)
    Fournisseur = models.ForeignKey(Fournisseur, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.libelle +" | "+ self.description +" | "+str(self.prix) +" | Type : "+self.type+ " | categorie : "+ str(self.Categorie)+" | fournisseur : "+str(self.Fournisseur) 

class ProduitNC(produit):
    Duree_garantie = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.libelle} - {self.Categorie} - {self.Fournisseur} - {self.Duree_garantie}"

class Commande (models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totalCde = models.DecimalField(max_digits=10, decimal_places=3)
    produits = models.ManyToManyField(produit)

    def __str__(self):
        return f"Commande du {self.dateCde} - {self.produits}" 
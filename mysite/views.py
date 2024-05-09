from django.shortcuts import render
from django.template import loader
from django.contrib.auth.decorators import login_required

@login_required
def acceuil(request):
    context = {'Value' : "Menu Accueil"}
    return render(request,'acceuil.html',context )
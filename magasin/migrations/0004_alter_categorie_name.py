# Generated by Django 5.0.2 on 2024-02-24 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('magasin', '0003_categorie_produit_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorie',
            name='name',
            field=models.CharField(choices=[('Al', 'Alimentaire'), ('Mb', 'Meuble'), ('Sn', 'Sanitaire'), ('Vs', 'Vaisselle'), ('Vt', 'Vêtement'), ('Jx', 'Jouets'), ('Ec', 'Electronique'), ('Hm', 'Immeuble'), ('Fa', 'Frais'), ('Ta', 'Tapis'), ('Lg', 'Linge de Maison'), ('Bj', 'Bijoux'), ('Dc', 'Décor')], default='Alimentaire', max_length=50),
        ),
    ]

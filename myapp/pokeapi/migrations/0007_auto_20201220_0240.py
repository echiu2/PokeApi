# Generated by Django 3.1.4 on 2020-12-20 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapi', '0006_auto_20201220_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='mega_evolution',
            field=models.BooleanField(),
        ),
    ]
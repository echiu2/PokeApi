from django.db import models

# Create your models here.
class Pokemon(models.Model):
    number = models.IntegerField()
    code = models.IntegerField()
    serial = models.IntegerField()
    name = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    ability1 = models.CharField(max_length=100)
    ability2 = models.CharField(max_length=100)
    hidden_ability = models.CharField(max_length=100)
    generation = models.IntegerField()
    legendary = models.BooleanField()
    mega_evolution = models.BooleanField()
    height = models.FloatField()
    weight  = models.FloatField()
    hp = models.IntegerField()
    attack = models.IntegerField()
    defense = models.IntegerField()
    special_attack = models.IntegerField()
    special_defense = models.IntegerField()
    speed = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.name
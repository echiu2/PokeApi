from django.db import models
from adaptor.model import CsvModel
from adaptor.fields import IntegerField, CharField, BooleanField, FloatField
from .models import Pokemon

# Create your models here.
class PokemonCsv(CsvModel):
    number = IntegerField()
    code = IntegerField()
    serial = IntegerField()
    name = CharField()
    type1 = CharField()
    type2 = CharField()
    color = CharField()
    ability1 = CharField()
    ability2 = CharField()
    hidden_ability = CharField()
    generation = IntegerField()
    legendary = IntegerField()
    mega_evolution = IntegerField()
    height = FloatField()
    weight  = FloatField()
    hp = IntegerField()
    attack = IntegerField()
    defense = IntegerField()
    special_attack = IntegerField()
    special_defense = IntegerField()
    speed = IntegerField()
    total = IntegerField()

    class Meta:
        dbModel = Pokemon
        delimiter = ","
        has_header = True

    # def __str__(self):
    #     return self.name
from django.db import models


class Pokemon(models.Model):
    id_pokemon = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    type1 = models.CharField(max_length=100, null=True, blank=True)
    type2 = models.CharField(max_length=100, null=True, blank=True)
    total = models.IntegerField(null=True, blank=True)
    hp = models.IntegerField( null=True, blank=True)
    attack = models.IntegerField(null=True, blank=True)
    defense = models.IntegerField(null=True, blank=True)
    sp_atk = models.IntegerField(null=True, blank=True)
    sp_def = models.IntegerField(null=True, blank=True)
    speed = models.IntegerField(null=True, blank=True)
    generation = models.IntegerField( null=True, blank=True)
    legendary = models.BooleanField(default=False)
    class Meta:
        db_table="pokemonApp_pokemon"

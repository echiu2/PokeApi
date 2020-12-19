from django.db import models

# Create your models here.
class Pokemon(models.Model):
    code = models.IntegerField()
    serial = models.IntegerField()
    name = models.CharField(max_length=100)
    type1 = models.CharField(max_length=100)
    type2 = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.name
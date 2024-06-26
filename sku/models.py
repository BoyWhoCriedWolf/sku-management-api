from django.db import models

class Sku(models.Model):
    medication_name = models.CharField(max_length=500)
    dose = models.CharField(max_length=500)
    presentation = models.CharField(max_length=500)
    unit = models.CharField(max_length=50)
    countries = models.CharField(max_length=500)

    def __str__(self):
        return self.name
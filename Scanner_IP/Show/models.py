from django.db import models


# Create your models here.
class Save_Info(models.Model):
    quantity = models.CharField(max_length=30)
    color = models.CharField(max_length=30)
    lat = models.DecimalField(max_digits=9, decimal_places=6)
    lon = models.DecimalField(max_digits=9, decimal_places=6)
    Address = models.CharField(max_length=40)

    def __str__(self):
        template = '{0.id} {0.quantity} {0.color} {0.Address}'
        return template.format(self)
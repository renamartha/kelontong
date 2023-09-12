from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    harga = models.IntegerField()
    tanggal = models.DateField(auto_now_add=True)
    description = models.TextField()
# Create your models here.

from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    amount = models.IntegerField()
    harga = models.IntegerField()
    tanggal = models.DateField(auto_now_add=True)
    description = models.TextField()
# Create your models here.

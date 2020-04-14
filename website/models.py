from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Buyyer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    mobile = models.CharField(max_length=15)
    ostan = models.CharField(max_length=60)
    city = models.CharField(max_length=70)
    code = models.CharField(max_length=6)
    address = models.TextField()

    def __str__(self):
        return self.user.username
    

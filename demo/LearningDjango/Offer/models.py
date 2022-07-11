from django.db import models

# Create your models here.
class Offer(models.Model):
    code=models.CharField(max_length=7)
    description=models.CharField(max_length=2000)
    discount=models.FloatField()
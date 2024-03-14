from django.db import models 
class Products(models.Model):
    name = models.CharField(max_length=1000)
    description = models.TextField()

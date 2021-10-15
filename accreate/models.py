from django.db import models

# Create your models here.
from django.contrib.auth.models import User



class Catalog(models.Model):



    user=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    common=models.CharField(max_length=50)
    botanical=models.CharField(max_length=100)
    zone=models.IntegerField()
    light=models.CharField(max_length=50)
    price=models.CharField(max_length=100)
    acaıkabıkıty=models.IntegerField()


    def __str__(self):

        return self.common




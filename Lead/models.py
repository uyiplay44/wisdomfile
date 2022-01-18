import email
from pyexpat import model
from django.db import models

# Create your models here.

class User(models.Model):
    name= models.CharField(max_length=300)


    def ___str____(self):
        return self.name



class  Profile(models.Model):
    User = models.OneToOneField (User, on_delete=models.CASCADE)
    address = models.CharField(max_length=300, default= '71 brick')
    email = models.EmailField(max_length=300, default='uyiplay44@hotmail.com')
    age = models.IntegerField (default=1)

    def __str__(self):
        return f'{self.email} ----- {self.user.name}'


class  Profile(models.Model):
    User = models.OneToOneField (User, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=300, default= '71 brick')
    email = models.EmailField(max_length=300, default='uyiplay44@hotmail.com')
    age = models.IntegerField (default=1)

    def __str__(self):
        return self.email
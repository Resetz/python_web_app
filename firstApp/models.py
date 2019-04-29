from django.db import models

# Create your models here.
class Person(models.Model):
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    age= models.IntegerField()

    def __str__(self):
        return self.lastName+","+self.firstName


class LoginCred(models.Model):
    user= models.CharField(max_length=10)
    password= models.CharField(max_length=10)
    firstName= models.CharField(max_length=255)
    lastName= models.CharField(max_length=255)
    

    def __str__(self):
        return len(self.password) * "*" + ", " + self.user
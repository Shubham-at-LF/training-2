from django.db import models
from datetime import date

# Create your models here.

class user(models.Model):
    name = models.CharField(max_length = 200)
    profilePic = models.CharField(max_length =400)
    userSince = models.DateField(default = date.today)
    def __str__(self):
        return self.name + ""


class user_Post(models.Model):
    user = models.ForeignKey(user,on_delete = models.CASCADE)
    content = models.CharField(max_length  =2000)
    published_date = models.DateField(default = date.today)
    def __str__(self):
        return self.user.name + ""


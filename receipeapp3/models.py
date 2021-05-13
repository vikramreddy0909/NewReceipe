from django.db import models
from django.contrib.auth.models import User


class Receipe(models.Model):
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=200)
    process=models.CharField(max_length=250)
    ingridients=models.CharField(max_length=300)
    pub_date=models.DateTimeField()
    image=models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
class Studentuserinfo(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    marks_10th =models.IntegerField




# Create your models here.

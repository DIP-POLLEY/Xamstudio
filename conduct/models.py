from django.db import models

# Create your models here.
class details(models.Model):
    uname = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    pwd = models.CharField(max_length=1000)
    date = models.DateField()
    noques = models.IntegerField()
    starttime= models.TimeField()
    stoptime = models.TimeField()

class questions(models.Model):

    uname = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    pwd = models.CharField(max_length=1000)
    quest = models.CharField(max_length=1000)


    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    
    opb1 = models.BooleanField(default=False)
    opb2 = models.BooleanField(default=False)
    opb3 = models.BooleanField(default=False)
    opb4 = models.BooleanField(default=False)
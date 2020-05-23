from django.db import models

# Create your models here.
class tests(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)


class qsheet(models.Model):
    uname = models.CharField(max_length=100)
    nosub = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    option1 = models.CharField(max_length=1000)
    option2 = models.CharField(max_length=1000)
    option3 = models.CharField(max_length=1000)
    option4 = models.CharField(max_length=1000)
    
    opb1 = models.BooleanField(default=False)
    opb2 = models.BooleanField(default=False)
    opb3 = models.BooleanField(default=False)
    opb4 = models.BooleanField(default=False)

class anspap(models.Model):
    uname = models.CharField(max_length=100)
    nosub = models.CharField(max_length=100)
    question = models.CharField(max_length=1000)
    opb1 = models.BooleanField(default=False)
    opb2 = models.BooleanField(default=False)
    opb3 = models.BooleanField(default=False)
    opb4 = models.BooleanField(default=False)

class result(models.Model):
    uname = models.CharField(max_length=100)
    nosub = models.CharField(max_length=100)
    score = models.IntegerField()
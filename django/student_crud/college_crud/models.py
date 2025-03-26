from django.db import models

# Create your models here.
class College(models.Model):
    name = models.CharField(max_length=100)
    usn = models.CharField(max_length=20, unique=True)
    branch = models.CharField(max_length=50)
    sem = models.IntegerField()
    bookname = models.CharField(max_length=50)
    isbi = models.IntegerField()
    authorname = models.CharField(max_length=50)


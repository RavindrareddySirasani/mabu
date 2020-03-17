from django.db import models

# Create your models here.
class Empmodel(models.Model):
    eno=models.CharField(max_length=20)
    ename=models.CharField(max_length=20)
    file=models.FileField(upload_to='files',default='')
    image=models.ImageField(upload_to='images',default='')
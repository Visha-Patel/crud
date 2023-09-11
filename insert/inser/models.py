from django.db import models

class Collage(models.Model):
    name=models.CharField(max_length=40)
    email=models.EmailField(max_length=30)
    contact=models.IntegerField()
    rollno=models.CharField(max_length=13)
    course=models.CharField(max_length=15)
    clas=models.CharField(max_length=7)
    img=models.FileField(upload_to='images')

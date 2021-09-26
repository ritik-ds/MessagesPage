from django.db import models

# Create your models here.
class Text(models.Model):
    text=models.TextField(max_length=1024)

class Image(models.Model):
    photo=models.ImageField(upload_to='media/')
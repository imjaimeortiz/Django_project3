from django.db import models
from django.db.models.fields import CharField, DateField, TextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20, default='')
    pub_date = models.DateField(null=True)
    body = models.TextField(default='')
    image = models.ImageField(upload_to='images/', null=True)

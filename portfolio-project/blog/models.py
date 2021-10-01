from django.db import models
from django.db.models.fields import CharField, DateField, TextField

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:100]
    
    def print_date(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

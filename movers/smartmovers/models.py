from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Post(models.Model):
    Availability=[
       ( 'Available','Available'),
      (  'Anavailable','Unavailable'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=20,null=False)
    location = models.CharField(max_length=30, null=False)
    availability =models.CharField(choices=Availability,max_length=11,null=False)
    phone = models.IntegerField()
    vehicle_type= models.CharField(max_length=20,null=False)
    image = models.FileField(default='movers_pics/default.jpg', upload_to='movers_pics/')
    description = models.TextField(max_length=100,null=True)
    least_price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

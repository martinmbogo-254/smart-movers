from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.datetime import DateTimeField

# Create your models here.

class Post(models.Model):
    Availability=[
       ( 'Available','Available'),
      (  'Anavailable','Unavailable'),
    ]
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100, null=False)
    availability =models.CharField(choices=Availability,max_length=11,null=False)
    phone = models.IntegerField()
    vehicle_type= models.CharField(max_length=100,null=False)
    image = models.ImageField(upload_to='movers_pics/')
    description = models.TextField(max_length=150,null=True)
    # posted = models.DateTimeField(auto_now_add=True)
    least_price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,
     related_name='rating')
    Rate_choices=[
    ('Very Dissatisfied','1'),
    ('Dissatisfied','2'),
    ('Fair','3'),
    ('Satisfied','4'),
    ('Very Satisfied','5'),


    ]
    author = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    rate = models.CharField(choices=Rate_choices,max_length=50, null= True)
    comment = models.CharField(max_length=50, null=True)

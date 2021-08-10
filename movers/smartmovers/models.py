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
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100, null=False)
    availability =models.CharField(choices=Availability,max_length=11,null=False)
    phone = models.IntegerField()
    vehicle_type= models.CharField(max_length=100,null=False)
    image = models.FileField(upload_to='movers_pics/',default='movers_pics/default.jpg')
    description = models.TextField(max_length=150,null=True)

    least_price = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


RATE_CHOICES =[
            (1,'1-Very Dissatisfied'),
            (2,'2-Dissatisfied'),
            (3,'3-Fair'),
            (4,'4-Satisfied'),
            ( 5,'5-Very Satisfied'),
        ]
class Rating(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,null=True,
     related_name='rating')
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES,max_length=50, null= True)
    comment = models.CharField(max_length=100, null=True)

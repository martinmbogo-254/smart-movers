from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

from twilio.rest import Client
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
    image = models.FileField(default='movers_pics/default.jpg', upload_to='movers_pics/')
    description = models.TextField(max_length=150,null=True)
    posted = models.DateTimeField( auto_now_add=True,null=True)
    updated = models.DateTimeField( auto_now=True, null=True)



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
    posted = models.DateTimeField( auto_now_add=True,null= True)


class sms (models.Model):
    name = models.ForeignKey(User,on_delete=models.CASCADE)
    message = models.CharField(max_length=300,null=True)

    def __str__(self):
        return self.name.username

    def save(self,*args,**kwargs):
        account_sid = 'ACd29314508846a743414a69526ab99219'
        auth_token = '2df4f0ff325a629f4077c25c99b7e2dd'
        client = Client(account_sid, auth_token)

        message = client.messages.create(
                            body={self.message},
                            from_='+17038842547',
                            to='+254745499838'
                        )

        print(message.sid)
        return super().save(*args,**kwargs)


# Generated by Django 3.2.5 on 2021-08-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartmovers', '0028_remove_rating_posted'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='rating',
            name='posted',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]

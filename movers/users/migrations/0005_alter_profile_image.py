# Generated by Django 3.2.5 on 2021-08-17 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.FileField(default='profile_pics/default.jpg', upload_to='profile_pics/'),
        ),
    ]

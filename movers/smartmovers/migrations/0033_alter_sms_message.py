# Generated by Django 3.2.6 on 2021-08-18 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartmovers', '0032_sms'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sms',
            name='message',
            field=models.CharField(max_length=300, null=True),
        ),
    ]

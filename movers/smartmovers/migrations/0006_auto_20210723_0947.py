# Generated by Django 2.1.5 on 2021-07-23 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smartmovers', '0005_auto_20210722_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='phone',
            field=models.IntegerField(max_length=10),
        ),
    ]

# Generated by Django 2.1.5 on 2021-07-27 15:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('smartmovers', '0011_auto_20210726_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.CharField(choices=[('1', 'Very Dissatisfied'), ('2', 'Dissatisfied'), ('3', 'Fair'), ('4', 'Satisfied'), ('5', 'Very Satisfied')], max_length=50, null=True)),
                ('comment', models.CharField(max_length=50, null=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='smartmovers.Post')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='ratings',
            name='user',
        ),
        migrations.DeleteModel(
            name='Ratings',
        ),
    ]

# Generated by Django 5.0.1 on 2024-01-09 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('UserSignup', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersignup',
            name='fullname',
            field=models.CharField(default='Harsh Modi', max_length=50),
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-21 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contact',
            name='message',
            field=models.CharField(default='', max_length=200),
        ),
    ]

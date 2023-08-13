# Generated by Django 4.2.4 on 2023-08-12 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zomato', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='dish',
        ),
        migrations.AddField(
            model_name='order',
            name='dishes',
            field=models.ManyToManyField(blank=True, to='zomato.dish'),
        ),
    ]

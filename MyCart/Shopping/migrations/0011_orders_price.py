# Generated by Django 3.0.2 on 2020-04-03 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0010_orderupdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 3.0.2 on 2020-02-15 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0004_auto_20200215_1848'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='', upload_to='Shopping/static/Shopping/images'),
        ),
    ]

# Generated by Django 3.0.2 on 2020-03-24 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0009_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderUpdate',
            fields=[
                ('update_id', models.AutoField(primary_key=True, serialize=False)),
                ('order_id', models.IntegerField(default=0)),
                ('order_desc', models.CharField(max_length=5000)),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
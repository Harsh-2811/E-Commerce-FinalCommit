# Generated by Django 3.0.2 on 2020-03-04 12:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping', '0006_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('EnrollMent', models.CharField(max_length=30)),
                ('Branch', models.CharField(max_length=10)),
            ],
        ),
    ]

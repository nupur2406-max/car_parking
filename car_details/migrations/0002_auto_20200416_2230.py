# Generated by Django 3.0.5 on 2020-04-16 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_details', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='car_intime',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='car',
            name='car_outtime',
            field=models.CharField(max_length=10),
        ),
    ]

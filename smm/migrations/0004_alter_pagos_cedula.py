# Generated by Django 5.0.6 on 2024-06-12 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smm', '0003_alter_pagos_fechapago'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagos',
            name='cedula',
            field=models.IntegerField(),
        ),
    ]
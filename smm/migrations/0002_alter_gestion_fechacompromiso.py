# Generated by Django 5.0.6 on 2024-06-12 20:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestion',
            name='fechaCompromiso',
            field=models.DateTimeField(null=True),
        ),
    ]

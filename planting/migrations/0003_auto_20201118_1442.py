# Generated by Django 3.1.2 on 2020-11-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planting', '0002_auto_20201118_1440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantingrecord',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

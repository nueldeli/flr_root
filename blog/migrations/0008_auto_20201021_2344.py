# Generated by Django 3.1 on 2020-10-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20201020_1516'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_img',
            field=models.ImageField(blank=True, null=True, upload_to='media/uploads/', verbose_name='Thumbnail'),
        ),
    ]

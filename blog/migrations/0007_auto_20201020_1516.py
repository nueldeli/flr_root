# Generated by Django 3.1.2 on 2020-10-20 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20201020_1350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_img',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]

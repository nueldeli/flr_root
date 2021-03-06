# Generated by Django 3.1.2 on 2020-11-16 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20201109_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlantingRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_planted', models.DateTimeField()),
                ('programme_name', models.CharField(max_length=250)),
                ('programme_img', models.ImageField(blank=True, null=True, upload_to='programme_img/', verbose_name='Programme Image')),
                ('location', models.CharField(max_length=250)),
                ('region', models.CharField(max_length=250)),
                ('area', models.FloatField()),
                ('species', models.CharField(max_length=255)),
                ('participants', models.CharField(max_length=250)),
            ],
        ),
        migrations.AlterField(
            model_name='treespeciesdata',
            name='quantity',
            field=models.IntegerField(null=True, verbose_name='Total'),
        ),
    ]

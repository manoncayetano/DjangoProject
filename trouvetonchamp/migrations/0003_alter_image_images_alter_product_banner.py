# Generated by Django 4.1.5 on 2023-01-29 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trouvetonchamp', '0002_rename_images_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.ImageField(upload_to='static/product/images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='banner',
            field=models.ImageField(upload_to='static/media/banner'),
        ),
    ]

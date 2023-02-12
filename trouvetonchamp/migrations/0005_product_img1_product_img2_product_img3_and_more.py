# Generated by Django 4.1.5 on 2023-01-31 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trouvetonchamp', '0004_alter_image_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='img1',
            field=models.ImageField(null=True, upload_to='static/media/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='img2',
            field=models.ImageField(null=True, upload_to='static/media/img'),
        ),
        migrations.AddField(
            model_name='product',
            name='img3',
            field=models.ImageField(null=True, upload_to='static/media/img'),
        ),
        migrations.AlterField(
            model_name='image',
            name='images',
            field=models.ImageField(upload_to='static/product/images'),
        ),
    ]

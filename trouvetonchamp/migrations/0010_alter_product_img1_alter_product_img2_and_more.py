# Generated by Django 4.1.5 on 2023-02-03 08:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trouvetonchamp', '0009_alter_product_img1_alter_product_img2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img1',
            field=models.ImageField(blank=True, default='NULL', null=True, upload_to='static/media/img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img2',
            field=models.ImageField(blank=True, default='NULL', null=True, upload_to='static/media/img'),
        ),
        migrations.AlterField(
            model_name='product',
            name='img3',
            field=models.ImageField(blank=True, default='NULL', null=True, upload_to='static/media/img'),
        ),
    ]

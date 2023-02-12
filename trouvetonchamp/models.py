from datetime import datetime

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True, default='')

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True, default='')
    banner = models.ImageField(upload_to='static/media/banner')
    img2 = models.ImageField(upload_to='static/media/img', null=True, blank=True)
    img1 = models.ImageField(upload_to='static/media/img', null=True, blank=True)
    img3 = models.ImageField(upload_to='static/media/img', null=True, blank=True)
    summary = models.CharField(max_length=200, null=True, blank=True, default='')
    content = models.TextField(null=True, blank=True, default='')
    date_pub = models.DateTimeField(default=datetime.now, blank=True)

    categories = models.ManyToManyField(Category, related_name='products')
    users = models.ForeignKey(User, related_name='users', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} / {self.users} / {self.date_pub}"


class Image(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True, blank=True)
    images = models.ImageField(upload_to='static/product/images')

    def __str__(self):
        return f"{self.id} - {self.product.name} "



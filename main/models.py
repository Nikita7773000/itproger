from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField('Название', max_length=50)
    author = models.CharField('краткое описание', max_length=50)
    title = models.TextField('полное Описание')
    date = models.IntegerField('Дата ')

    my_image = models.ImageField(upload_to='images/')


class Product(models.Model):
    name = models.CharField('Название', max_length=100)
    category = models.CharField('Категория', max_length=100)
    summary = models.CharField('краткое описание', max_length=100)
    full_content = models.TextField('полное описание')
    price = models.FloatField('цена')
    quantity = models.IntegerField('количество на складе')


class Comment(models.Model):
    comment = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comment')
    my_comment = models.TextField('Комментарий')



class Oven(models.Model):
    oven = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='oven')
    my_oven = models.IntegerField('оценка')

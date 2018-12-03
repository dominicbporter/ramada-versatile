from django.db import models


class Hotel(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    html_dir = models.CharField(max_length=32)
    img_dir = models.CharField(max_length=32)
    info_dir = models.CharField(max_length=32)


class Contact(models.Model):
    manager = models.CharField(max_length=32)
    email = models.EmailField()
    phone = models.IntegerField()
    facebook = models.URLField()
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)


class Room(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    img_dir = models.CharField(max_length=64)
    book = models.CharField(max_length=64)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)


class Facilities(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    img_dir = models.CharField(max_length=64)
    hotel = models.ForeignKey('Hotel', on_delete=models.CASCADE)

from django.db import models


class Contact(models.Model):
    manager = models.CharField(max_length=32, default="Manager's Name")
    email = models.EmailField(max_length=64, default="contact@ramada.nz")
    phone = models.CharField(max_length=12, default="010")
    facebook = models.URLField(max_length=128, default="facebook.com/ramadanz")

    def __str__(self):
        return self.manager


class Hotel(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    html_dir = models.CharField(max_length=32)
    img_dir = models.CharField(max_length=32)
    info_dir = models.CharField(max_length=32)
    contact = models.OneToOneField(
        Contact,
        on_delete=models.CASCADE,
    )
    room = models.ForeignKey('Room',
                             on_delete=models.CASCADE,
                             related_name='rooms')

    def __str__(self):
        return self.name


class Room(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    img_dir = models.CharField(max_length=64)
    book = models.CharField(max_length=64)

    def __str__(self):
        return self.name + "-"


class Facilities(models.Model):
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    img_dir = models.CharField(max_length=64)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + "-" + self.hotel.name

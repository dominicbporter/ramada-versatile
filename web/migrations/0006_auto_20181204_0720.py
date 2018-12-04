# Generated by Django 2.1.3 on 2018-12-04 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20181204_0711'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='contact@ramada.nz', max_length=64),
        ),
        migrations.AddField(
            model_name='contact',
            name='facebook',
            field=models.URLField(default='facebook.com/ramadanz', max_length=128),
        ),
        migrations.AddField(
            model_name='contact',
            name='manager',
            field=models.CharField(default="Manager's Name", max_length=32),
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.IntegerField(default='', max_length=12),
        ),
    ]

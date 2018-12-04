# Generated by Django 2.1.3 on 2018-12-04 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0011_auto_20181204_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(default="Manager's Name", max_length=32)),
                ('email', models.EmailField(default='contact@ramada.nz', max_length=64)),
                ('phone', models.CharField(default='010', max_length=12)),
                ('facebook', models.URLField(default='facebook.com/ramadanz', max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Facilities',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('img_dir', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Hotel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('html_dir', models.CharField(max_length=32)),
                ('img_dir', models.CharField(max_length=32)),
                ('info_dir', models.CharField(max_length=32)),
                ('contact', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.Contact')),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=512)),
                ('img_dir', models.CharField(max_length=64)),
                ('book', models.CharField(max_length=64)),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Hotel')),
            ],
        ),
        migrations.CreateModel(
            name='RoomLink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Hotel', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.Hotel')),
                ('Room', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='web.Room')),
            ],
        ),
        migrations.AddField(
            model_name='facilities',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.Hotel'),
        ),
    ]

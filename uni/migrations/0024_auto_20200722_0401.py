# Generated by Django 3.0.7 on 2020-07-21 23:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0023_auto_20200721_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='forget',
            name='a',
        ),
        migrations.RemoveField(
            model_name='forget',
            name='bs',
        ),
    ]
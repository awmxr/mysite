# Generated by Django 3.0.7 on 2020-07-18 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ostad',
            name='dars1',
        ),
        migrations.RemoveField(
            model_name='ostad',
            name='dars2',
        ),
        migrations.RemoveField(
            model_name='ostad',
            name='dars3',
        ),
        migrations.RemoveField(
            model_name='ostad',
            name='dars4',
        ),
    ]
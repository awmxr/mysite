# Generated by Django 3.0.7 on 2020-06-13 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0009_student_activate'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ostad',
            name='activate',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='ostad',
            name='online',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='student',
            name='online',
            field=models.BooleanField(default=False),
        ),
    ]

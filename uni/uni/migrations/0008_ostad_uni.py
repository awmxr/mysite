# Generated by Django 3.0.6 on 2020-06-13 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0007_remove_ostad_uni'),
    ]

    operations = [
        migrations.AddField(
            model_name='ostad',
            name='uni',
            field=models.CharField(default=' ', max_length=200),
            preserve_default=False,
        ),
    ]

# Generated by Django 3.0.6 on 2020-05-30 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0006_student_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='birthdate',
        ),
        migrations.AlterField(
            model_name='student',
            name='pub_date',
            field=models.DateTimeField(verbose_name='birthday'),
        ),
    ]
# Generated by Django 3.0.6 on 2020-06-03 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0014_auto_20200603_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='enter_year',
            field=models.CharField(choices=[('------------------------------------------------------------------------------', '------------------------------------------------------------------------------'), ('1400', '1400'), ('1399', '1399'), ('1398', '1398'), ('1397', '1397'), ('1396', '1396'), ('1395', '1395'), ('1394', '1394'), ('1393', '1393'), ('1392', '1392'), ('1391', '1391')], max_length=200),
        ),
        migrations.AlterField(
            model_name='student',
            name='field',
            field=models.CharField(choices=[('------------------------------------------------------------------------------', '------------------------------------------------------------------------------'), ('مهندسی کامپیوتر', 'مهندسی کامپیوتر'), ('مهندسی برق', 'مهندسی برق'), ('مهندسی عمران', 'مهندسی عمران'), ('مهندسی مکانیک', 'مهندسی مکانیک'), ('مهندسی شیمی', 'مهندسی شیمی'), ('مهندسی شهرسازی', 'مهندسی شهرسازی'), ('علوم کامپیوتر', 'علوم کامپیوتر'), ('ریاضی', 'ریاضی'), ('فیزیک', 'فیریک'), ('شیمی', 'شیمی'), ('معماری', 'معماری'), ('اقتصاد', 'اقتصاد'), ('علوم سیاسی', 'علوم سیاسی'), ('هنر', 'هنر'), ('معارف', 'معارف'), ('مدیریت', 'مدیریت')], max_length=200),
        ),
    ]

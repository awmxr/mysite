# Generated by Django 3.0.7 on 2020-07-21 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0022_auto_20200721_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin2',
            name='College',
            field=models.CharField(choices=[('------------------------------------------------------------------------------', '------------------------------------------------------------------------------'), ('1', 'فنی مهندسی'), ('2', 'علوم پایه'), ('3', 'علوم اقتصادی و اداری'), ('4', 'علوم سیاسی'), ('5', 'علوم دریایی')], max_length=2000),
        ),
        migrations.AlterField(
            model_name='admin2',
            name='ejaze',
            field=models.CharField(blank=True, max_length=10000),
        ),
        migrations.AlterField(
            model_name='admin2',
            name='uni',
            field=models.CharField(choices=[('------------------------------------------------------------------------------', '------------------------------------------------------------------------------'), ('1', 'تهران'), ('2', 'مازندران'), ('3', 'اصفهان'), ('4', 'امیر کبیر'), ('5', 'صنعتی شریف'), ('6', 'شهید بهشتی'), ('7', 'صنعتی اصفهان'), ('8', 'علم و صنعت'), ('9', 'خواجه نصیر'), ('10', 'شیراز'), ('11', 'نوشیروانی'), ('12', 'تبریز')], max_length=2000),
        ),
    ]
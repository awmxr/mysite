# Generated by Django 3.0.6 on 2020-06-13 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uni', '0005_auto_20200607_1715'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ostad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('melli_code', models.CharField(max_length=200)),
                ('uni', models.CharField(max_length=200)),
                ('College', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=11)),
                ('religion', models.CharField(max_length=200)),
                ('public_date', models.DateTimeField(null=True)),
                ('login_date', models.DateTimeField(null=True)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('login_times', models.CharField(max_length=10000)),
            ],
        ),
    ]

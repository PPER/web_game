# Generated by Django 2.2.1 on 2019-06-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0046_auto_20190603_1123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wonder_archive_people',
            name='health',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='wonder_archive_people',
            name='love',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='wonder_archive_people',
            name='money',
            field=models.IntegerField(default=100),
        ),
    ]
# Generated by Django 2.2 on 2019-05-13 04:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0027_wonder_archive_people_k'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wonder_archive_people',
            name='k',
        ),
    ]
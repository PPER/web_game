# Generated by Django 2.2 on 2019-04-10 11:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0010_auto_20190408_1230'),
    ]

    operations = [
        migrations.AddField(
            model_name='wonder_archive_people',
            name='active_state',
            field=models.IntegerField(default=0),
        ),
    ]

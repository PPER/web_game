# Generated by Django 2.2 on 2019-04-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0005_auto_20190402_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='story_file_status',
            name='last_figure_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='story_file_status',
            name='last_pic_url',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='story_file_status',
            name='last_sentence',
            field=models.CharField(default='本Archive尚未开启，请点击按钮建立', max_length=200),
        ),
        migrations.AddField(
            model_name='story_file_status',
            name='last_sound_url',
            field=models.CharField(default='', max_length=200),
        ),
    ]

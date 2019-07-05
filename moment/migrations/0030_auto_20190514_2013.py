# Generated by Django 2.2 on 2019-05-14 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0029_basic_setting'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story_file_status',
            name='last_figure_center_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='story_file_status',
            name='last_figure_left_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='story_file_status',
            name='last_figure_right_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='story_file_status',
            name='last_pic_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='story_file_status',
            name='last_sound_url',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]

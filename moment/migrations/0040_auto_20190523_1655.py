# Generated by Django 2.2 on 2019-05-23 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0039_auto_20190517_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story_file_status',
            name='last_sentence',
            field=models.CharField(default='请点击对话框继续游戏', max_length=200),
        ),
    ]
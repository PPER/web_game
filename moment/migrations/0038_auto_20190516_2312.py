# Generated by Django 2.2 on 2019-05-16 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0037_auto_20190516_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store_card_own',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moment.Wonder_Archive_People'),
        ),
        migrations.AlterField(
            model_name='store_card_own',
            name='store_card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moment.Store_Card'),
        ),
        migrations.AlterField(
            model_name='store_card_own',
            name='story_file_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='moment.Story_File_Status'),
        ),
        migrations.AlterField(
            model_name='wonder_archive_people',
            name='active_state',
            field=models.IntegerField(default=1),
        ),
    ]
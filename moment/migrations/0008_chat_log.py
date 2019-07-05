# Generated by Django 2.2 on 2019-04-06 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0007_story_file_status_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chat_Log',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=600)),
                ('chat_person', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='moment.Wonder_Archive_People')),
                ('story_file_status', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='moment.Story_File_Status')),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-05-09 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0018_store_card_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shopping_Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default=' ', max_length=200)),
                ('title', models.CharField(default=' ', max_length=50)),
                ('illustration', models.CharField(default=' ', max_length=200)),
                ('money', models.IntegerField(default=0)),
            ],
        ),
    ]

# Generated by Django 2.2 on 2019-05-12 00:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('moment', '0020_shopping_cart_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='shopping_cart',
            name='amount',
        ),
        migrations.CreateModel(
            name='Shopping_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('shopping_cart', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='moment.Shopping_Cart')),
                ('story_file_status', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='moment.Story_File_Status')),
            ],
        ),
    ]

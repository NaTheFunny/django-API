# Generated by Django 5.0.6 on 2024-06-25 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_post_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]
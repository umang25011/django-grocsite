# Generated by Django 4.1 on 2023-02-27 05:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0004_alter_post_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 0, 49, 28, 486454)),
        ),
    ]

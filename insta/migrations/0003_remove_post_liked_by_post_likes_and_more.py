# Generated by Django 4.1 on 2023-02-27 05:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_alter_profile_options_post_liked_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='liked_by',
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='liked_posts', to='insta.profile'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 27, 0, 35, 53, 994731)),
        ),
    ]

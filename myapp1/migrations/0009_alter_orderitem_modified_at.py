# Generated by Django 4.1 on 2023-02-06 19:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0008_rename_description_projectdescription_desc_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 6, 14, 18, 45, 374138)),
        ),
    ]

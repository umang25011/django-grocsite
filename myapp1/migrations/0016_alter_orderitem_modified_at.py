# Generated by Django 4.1 on 2023-03-07 18:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0015_alter_item_interested_alter_orderitem_modified_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='modified_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 3, 7, 13, 35, 9, 33882)),
        ),
    ]

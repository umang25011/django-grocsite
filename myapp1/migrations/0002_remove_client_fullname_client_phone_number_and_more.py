# Generated by Django 4.1 on 2023-01-31 19:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp1', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='fullname',
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='item_description',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')], default='CH', max_length=2),
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no_of_items', models.IntegerField(default=1)),
                ('status', models.IntegerField(choices=[(0, 'Cancelled'), (1, 'Placed'), (2, 'Shipped'), (3, 'Delivered')], default=1)),
                ('modified_at', models.DateTimeField(default=datetime.datetime(2023, 1, 31, 14, 7, 56, 839423))),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='myapp1.client')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='myapp1.item')),
            ],
        ),
    ]

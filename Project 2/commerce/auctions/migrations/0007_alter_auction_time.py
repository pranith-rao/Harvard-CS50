# Generated by Django 3.2.3 on 2021-05-22 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_auction_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auction',
            name='time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]

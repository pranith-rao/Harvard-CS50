# Generated by Django 3.2.3 on 2021-05-22 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_alter_auction_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='auction',
            name='user',
            field=models.CharField(default='some', max_length=64),
        ),
    ]

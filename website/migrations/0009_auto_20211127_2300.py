# Generated by Django 3.2.8 on 2021-11-27 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0008_auto_20211127_2155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bid',
            old_name='currentBidAmount',
            new_name='bidAmount',
        ),
        migrations.AddField(
            model_name='product',
            name='basePrice',
            field=models.FloatField(default=0.0),
        ),
    ]

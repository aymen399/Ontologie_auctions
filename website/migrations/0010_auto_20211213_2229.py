# Generated by Django 3.2.8 on 2021-12-13 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20211127_2300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='number_of_bids',
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('LAP', 'Laptop'), ('CON', 'Console'), ('GAD', 'Gadget'), ('GAM', 'Game'), ('TEL', 'TV'), ('sh', 'shareable')], max_length=200),
        ),
    ]
# Generated by Django 3.1 on 2021-11-25 06:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0005_batchintegrity_offline_wallet_sent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batchintegrity',
            name='offline_wallet_sent',
            field=models.CharField(default='{}', max_length=255),
        ),
    ]
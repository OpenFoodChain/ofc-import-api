# Generated by Django 3.1 on 2021-11-24 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0003_auto_20211124_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batchintegrity',
            name='offline_wallet_sent',
        ),
    ]
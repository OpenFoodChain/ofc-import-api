# Generated by Django 3.1 on 2022-09-21 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0103_merge_20220902_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='mass',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
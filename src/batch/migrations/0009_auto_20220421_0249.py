# Generated by Django 3.1 on 2022-04-21 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0008_auto_20220421_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batch',
            name='bnfp',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]
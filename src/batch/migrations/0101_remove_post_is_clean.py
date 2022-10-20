from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('batch', '0100_someitem_is_clean'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='batch',
            name='is_clean',
        ),
    ]
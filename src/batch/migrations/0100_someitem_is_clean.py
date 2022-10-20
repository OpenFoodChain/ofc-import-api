from django.db import migrations, models

class Migration(migrations.Migration):
    """Migration to add ``is_clean`` field to ``Organization``"""

    dependencies = [
        ('batch', '0009_auto_20220421_0249'),
    ]

    operations = [
        migrations.AddField(
            model_name='batch',
            name='is_clean',
            field=models.BooleanField(default=True)
        )
    ]
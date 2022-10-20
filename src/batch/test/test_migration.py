import pytest
import os
import django
from django.conf import settings
from dotenv import load_dotenv
from django_test_migrations.migrator import Migrator
from django_test_migrations.plan import all_migrations, nodes_to_tuples

load_dotenv()

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

django.setup()

@pytest.mark.django_db(True)
def test_run_migration():
    migrator = Migrator(database='default')

    old_state = migrator.apply_initial_migration(('batch', '0009_auto_20220421_0249'))
    Batch = old_state.apps.get_model('batch', 'Batch')

    new_state = migrator.apply_tested_migration(('batch', '0100_someitem_is_clean'))
    Batch = new_state.apps.get_model('batch', 'Batch')

    assert len(Batch._meta.get_fields()) == 19

    migrator.reset()

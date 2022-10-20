from django.apps import AppConfig
import os
from helpers.logging import log

def startup():
  log("logs/import-api.log", 'BATCH IMPORT API STARTING', 'INFO')

class BatchConfig(AppConfig):
    name = 'batch'
    def ready(self):
        if os.environ.get('RUN_MAIN'):
            startup()


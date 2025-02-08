import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "schedule.settings")
django.setup()
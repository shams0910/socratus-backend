from django.db.models.signals import post_save
from django.core.management import call_command
from django.dispatch import receiver
from tenants.models import School
from tenants.utils import get_apps


@receiver(post_save, School)
def run_migrations_for_new_schema(sender, **kwargs):
    instance = kwargs['instance']
    schema = instance.get_schema_name()
    apps = get_apps
    for app in apps:
        call_command('migrate_new_schema', app_label=app, schema=schema)

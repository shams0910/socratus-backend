from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection
from tenants.models import School


class Command(MigrationCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            schemas = [school.get_schema_name()
                       for school in School.objects.all()]

            for schema in schemas:
                cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {schema}')
                cursor.execute(f'set schema_path to {schema}')
                super(Command, self).handle(*args, **options)

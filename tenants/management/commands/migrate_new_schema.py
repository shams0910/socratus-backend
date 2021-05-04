from django.core.management.commands.migrate import Command as MigrationCommand
from django.db import connection


class Command(MigrationCommand):
    def add_arguments(self, parser):
        parser.add_argument('schema', type=str)

    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            schema = options['schema']
            cursor.execute(f'CREATE SCHEMA IF NOT EXISTS {schema}')
            cursor.execute(f'set schema_path to {schema}')
            super(Command, self).handle(*args, **options)

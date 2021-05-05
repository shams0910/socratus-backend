from django.db import connection
from django.apps import apps


def get_apps(tenants=False):
    app_names = []
    if tenants:
        app_names = [app.name for app in apps.get_app_configs()]
    else:
        app_names = [app.name for app in apps.get_app_configs() if app.name != 'tenants']
    return app_names


def tenant_schema_from_request(request):
    tenant_schema = request.headers.get('tenant')
    return tenant_schema


def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path to {schema}')

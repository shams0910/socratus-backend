from django.db import connection


def get_apps():
    return ['accounts', ]


def tenant_schema_from_request(request):
    tenant_schema = request.headers.get('tenant')
    return tenant_schema


def set_tenant_schema_for_request(request):
    schema = tenant_schema_from_request(request)
    with connection.cursor() as cursor:
        cursor.execute(f'SET search_path to {schema}')

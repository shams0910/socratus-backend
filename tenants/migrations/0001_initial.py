# Generated by Django 3.1.4 on 2021-05-16 09:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Division',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('type', models.SmallIntegerField(choices=[(1, 'shahar'), (2, 'tuman')], null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('division', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.division')),
            ],
        ),
        migrations.CreateModel(
            name='RegionAdminProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tenants.region')),
            ],
        ),
        migrations.AddField(
            model_name='division',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='tenants.region'),
        ),
        migrations.AddConstraint(
            model_name='school',
            constraint=models.UniqueConstraint(fields=('number', 'division'), name='unique_school_in_division'),
        ),
    ]

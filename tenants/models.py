from django.db import models
from accounts.models import Account
# Create your models here.


class Region(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=20)


class RegionAdminProfile(models.Model):
    account = models.OneToOneField(Account, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)


class Division(models.Model):
    DIVISION_TYPE_CHOICES = ((1, "shahar"), (2, 'tuman'))

    name = models.CharField(max_length=30)
    region = models.ForeignKey(Region, on_delete=models.PROTECT)
    type = models.SmallIntegerField(choices=DIVISION_TYPE_CHOICES, null=True)


class School(models.Model):
    number = models.IntegerField()
    division = models.ForeignKey(Division, on_delete=models.PROTECT)

    class Meta:
        constraints = [models.UniqueConstraint(fields=['number', 'division'], name="unique_school_in_division")]

    def get_schema_name(self):
        return f'_{self.division_id}_{self.number}'

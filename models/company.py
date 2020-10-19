from django.conf import settings
from django.db import models
from django.utils import timezone


class Company(models.Model):
    id = models.IntegerField(primary_key=True)
    company = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_company'

    # def __str__(self):
    #     return self.company

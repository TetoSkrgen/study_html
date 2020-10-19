from django.conf import settings
from django.db import models
from django.utils import timezone

from . import Company


class Member(models.Model):
    test = models.ForeignKey('Company', primary_key=True,
                             on_delete=models.CASCADE, db_column='id')
    name = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 't_member'

    def __str__(self):
        return self.name

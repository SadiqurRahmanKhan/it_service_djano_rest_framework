from django.db import models
from .models import LedgerGroup, PrimaryGroup
# Primary Group and ledger group vertual model


class JoinPrimaryGroupLedgerModel(models.Model):
    id = models.IntegerField(primary_key=True)
    lgname = models.CharField(max_length=50)
    pgname = models.CharField(max_length=50)
    upgname = models.CharField(max_length=50)
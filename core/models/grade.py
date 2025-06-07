# to do

from django.db import models


class Grade(models.Model):

    nota = models.FloatField
    unidade = models.PositiveIntegerField

    def __str__(self) -> str:
        return super().__str__()

# to do
from django.db import models


class Subject(models.Model):
    id_subject = models.IntegerField
    name = models.CharField(max_length=40)
    code = models.IntegerField
    horario = models.CharField(max_length=10)

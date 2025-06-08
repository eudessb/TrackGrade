# to do
from django.db import models
from django.forms import ModelForm

from .usuario import User


HORARIO_CHOICES = sorted([ (15,"15HRS"),(30, "30HRS"),(45,"45HRS"),(60,"60HRS"),(90,"90HRS")], key = lambda x:x[1])
class Subject(models.Model):
    name = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10,unique=True,)
    carga_horaria = models.IntegerField(null=False,choices=HORARIO_CHOICES)
    alunos = models.ManyToManyField(User, related_name='disciplinas')

    def __str__(self) -> str:
        return self.name
    
    
# to do
from django.db import models
from django.forms import ModelForm

from .usuario import User


HORARIO_CHOICES = sorted([(30, "30HRS"),(60,"60HRS"),(90,"90HRS")], key = lambda x:x[1])
SEMESTRE_CHOICES = sorted([("2025.1","2025.1"),("2024.2","2024.2"),("2024.2","2024.2"),("2024.1","2024.1"),("2023.2","2023.2"),("2023.1","2023.1"),("2022.2","2022.2"),("2022.1","2022.1")] ,key=lambda x:x[-1] )
class Subject(models.Model):    
    name = models.CharField(max_length=40)
    codigo = models.CharField(max_length=10,unique=True)
    carga_horaria = models.IntegerField(null=False,choices=HORARIO_CHOICES)
    semestre = models.CharField(choices=SEMESTRE_CHOICES,default="2025.1")
    alunos = models.ManyToManyField(User, related_name='disciplinas')

    def __str__(self) -> str:
        return self.name
    
    
# to do

from django.db import models

from .usuario import User

from .subject import Subject

CHOICES = sorted([("1","1ª unidade "),("2","2ª unidade"),("3","3ª unidade ")], key= lambda x:x[1])
class Grade(models.Model):
    
    unidade = models.CharField(max_length=1,choices=CHOICES)
    nota = models.FloatField()
    disciplina = models.ForeignKey(Subject, on_delete=models.CASCADE,related_name='notas')
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='usuario')
    

    def __str__(self) -> str:
        return self.unidade

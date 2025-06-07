# to do
from django.db import models
from django.forms import ModelForm

class Subject(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField(default= 0)
    horario = models.CharField(max_length=10)

    def __str__(self) -> str:
        return self.name
    
    
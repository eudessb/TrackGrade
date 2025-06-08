from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from core.models import Subject
from core.models import User

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['name','codigo','carga_horaria']
        labels = {'name':'Nome da disciplina', 'codigo': 'Código da disciplina', 'carga_horaria': 'Carga horária',}
        help_texts = {'name': 'Exemplo: Banco de dados', 'codigo':'Exemplo: IMD0401', }
    def clean_codigo(self):
        codigo = self.cleaned_data['codigo']
        if Subject.objects.filter(codigo = codigo).exists():
            raise forms.ValidationError("Já existe uma   disciplina com este código.")
        
        return codigo
    
class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
    
class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = User
        fields = ("email",)
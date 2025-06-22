from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
    UserChangeForm,
    AuthenticationForm,
)
from core.models import Subject
from core.models import User
from core.models.grade import Grade


class SubjectForm(ModelForm):
    codigo = forms.CharField(max_length=10, label="Código da disciplina")
    class Meta:
        model = Subject
        fields = ["name", "codigo", "carga_horaria","semestre"]
        labels = {
            "name": "Nome da disciplina",
            "codigo": "Código da disciplina",
            "carga_horaria": "Carga horária",
            "semestre":"Semestre",
        }
        help_texts = {
            "name": "Exemplo: Banco de dados",
            "codigo": "Exemplo: IMD0401",
        }
    def validate_unique(self): # Override para ignorar validação automática de unicidade
            pass



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("email",)
        labels = {
            "email": "Endereço de email",
        }
        help_texts = {
            "email": "Exemplo: meuemail@gmail.com",
        }

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "Já existe um usuário cadastrado com este email"
            )
        return email
class CustomUserChangeForm(UserChangeForm):
    class meta:
        model = User
        fields = ("email",)

class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = {"email",}

class GradesForm(ModelForm):
    class Meta:
        model = Grade
        fields = ["unidade", "nota"]

        labels = {
            "unidade": "Unidade",
            "nota": "Nota",
            "disciplina": "Disciplina",
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user",None)  # pega o usuário passado pela view
        super().__init__(*args, **kwargs)
        if "disciplina" in self.fields and user:
            self.fields["disciplina"].queryset = user.disciplinas.all() # type: ignore
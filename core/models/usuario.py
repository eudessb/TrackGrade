from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.base_user import BaseUserManager
from django.utils import timezone

user_type_choices = sorted([('aluno', 'Aluno'), ('professor', 'Professor'), ], key = lambda x:x[1])


    
class UserManager(BaseUserManager):
    def create_user(self,email,password, **extra_fields):
        
        if not email:
            raise ValueError(_("Um email deve ser definido"))
        email = self.normalize_email(email)
        user = self.model(email=email,**extra_fields)
        user.set_password(password)
        user.save()
        return user
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff" ) is not True:
            raise ValueError(_("Superusuário deve ter is_staff=True."))
        if extra_fields.get("is_superuser" ) is not True:
            raise ValueError(_("Superusuário deve ter is_superuser=True."))
        return self.create_user(email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"),unique= True, blank=False)
    tipo = models.CharField(max_length=9    ,choices=user_type_choices, blank=False, default="aluno")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['tipo']
    
    objects = UserManager()
    def __str__(self) -> str:
        return self.email
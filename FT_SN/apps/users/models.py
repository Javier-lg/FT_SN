from django.db import models
from apps.core.models import Person

from django.contrib.auth.models import AbstractUser
from apps.users.manager import UserManager

# Create your models here.

class User(Person,AbstractUser):
    '''
    Modelo para usuario del sistema
    '''
    ROLE = [
        ('Administrador','Administrador'),
        ('Jugador','Jugador'),
        ('Organizador','Organizador')
    ]

    objects = UserManager()
    role = models.CharField(max_length=15, choices=ROLE, default='Jugador', null=True, blank=True)
    username = models.CharField(max_length=50, unique=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =['email','first_name','last_name','birth_date','id_number']

    def __str__(self):
        return f"{self.get_full_name()} | {self.phone_number or 'Sin telefono'} | {self.role}"
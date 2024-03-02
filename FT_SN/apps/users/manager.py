from django.contrib.auth.models import BaseUserManager
from django.urls import reverse

class UserManager(BaseUserManager):
    '''
    Manager de usuario
    '''
    '''
    Devuelve usuarios no eliminados
    '''
    def all(self):
        users = self.filter(deleted_at=None)
        return users
    
    
    def get_owner(self,pk):
        '''
        Devuelve un organizadores
        '''
        owner = self.get(pk=pk, role='Organizador',is_staff=False,is_superuser=False)
        return owner
       
    
    def get_employees(self):
        '''
        Devuelve los jugadores
        '''
        player = self.filter(role='Jugador',is_staff=False,is_superuser=False)
        return player
    
    def get_admins(self):
        '''
        Devuelve desarrolladores
        '''
        admins = self.filter(role='Administrador',is_staff=True,is_superuser=True)
        return admins
    
    def _create_user(self, first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields):
        user = self.model(
            first_name = first_name,
            last_name = last_name,
            username=username,
            email=email,
            is_staff=is_staff,
            is_superuser=is_superuser,
            role= role,
            **extra_fields
        )
        user.set_password(password)
        user.save()
        return user

    def create_player(self, first_name, last_name, username, email, password, **extra_fields): # Para Jugadores
        is_staff = False
        is_superuser = False
        role = 'Jugador'
        return self._create_user(first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields)

    def create_superuser(self, first_name, last_name, username, email, password, **extra_fields): # Para Desarrollador
        is_staff = True
        is_superuser = True
        role = 'Administrador'
        return self._create_user(first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields)
    
    def create_owner(self, first_name, last_name, username, email, password, **extra_fields): # Para Organizadores
        is_staff = False
        is_superuser = False
        role = 'Organizador'
        return self._create_user(first_name, last_name, username, email, password, is_staff, is_superuser, role, **extra_fields)
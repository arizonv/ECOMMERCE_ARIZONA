import re
from django.db import models
from django.core import validators
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, UserManager
)

class User(AbstractBaseUser, PermissionsMixin):
    
    ADMIN = 'A'
    TRABAJADOR = 'T'
    CLIENTE = 'C'
    TIPO_DE_USUARIO_CHOICES = [
        (ADMIN, 'Administrador'),
        (TRABAJADOR, 'Trabajador'),
        (CLIENTE, 'Cliente'),
    ]
    
    username = models.CharField(
        'Usuario', max_length=30, unique=True, validators=[
            validators.RegexValidator(
                re.compile('^[\w.@+-]+$'),
                'ingrese un nombre de usuario valido '
                'Este valor debe contener solo letras, números '
                'excepto: @/./+/-/_.'
                ,  'invalid'
            )
        ], help_text='Un nombre corto que sera usado'+
                    ' para identificarlo de forma unica en la plataforma.'
    )
    
    name = models.CharField('Name', max_length=100)
    email = models.EmailField('Email', unique=True)
    is_staff = models.BooleanField('Admin', default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)
    
    tipo_de_usuario = models.CharField(
        max_length=1,
        choices=TIPO_DE_USUARIO_CHOICES,
        default=CLIENTE,
    )

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return self.name or self.username
    
    def get_full_name(self):
        return str(self)

    def get_short_name(self):
        return str(self).split(' ')[0]

    def save(self, *args, **kwargs):
        if self.pk is not None:  # Verifica si el objeto ya está guardado en la base de datos
            old_instance = User.objects.get(pk=self.pk)  # Obtiene la instancia anterior del objeto
            if old_instance.tipo_de_usuario != self.tipo_de_usuario and self.tipo_de_usuario == self.ADMIN:
                self.is_staff = True  # Establece is_staff en True si el usuario cambia a ADMIN
            elif old_instance.tipo_de_usuario == self.ADMIN and self.tipo_de_usuario != self.ADMIN:
                self.is_staff = False  # Establece is_staff en False si el usuario deja de ser ADMIN
        super().save(*args, **kwargs)

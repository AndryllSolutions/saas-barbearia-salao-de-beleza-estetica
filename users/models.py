from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ("admin", "Administrador"),
        ("funcionario", "Funcionário"),
        ("cliente", "Cliente"),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="cliente")
    
    def __str__(self):
        return self.username
    
    def is_admin(self):
        return self.role == 'admin'

    def is_funcionario(self):
        return self.role == 'funcionario'

    def is_cliente(self):
        return self.role == 'cliente'

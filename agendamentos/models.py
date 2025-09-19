from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db import models

# Create your models here.


class Cliente(models.Model):
    usuario = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        null=True, blank=True,  # 🔥 permite que nem todo cliente tenha login
        related_name="perfil_cliente"
    )
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Servico(models.Model):
    nome = models.CharField(max_length=100)
    duracao = models.IntegerField(help_text="Duração em minutos")
    preco = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.nome

class Agendamento(models.Model):
    STATUS_CHOICES = [
        ("pendente", "Pendente"),
        ("concluido", "Concluído"),
        ("cancelado", "Cancelado"),
    ]

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    servico = models.ForeignKey(Servico, on_delete=models.CASCADE)
    usuario = models.ForeignKey("users.User", on_delete=models.CASCADE)
    data = models.DateField()
    hora = models.TimeField()
    criado_em = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pendente")  # 🔥 novo

    def __str__(self):
        return f"{self.cliente.nome} - {self.servico.nome} ({self.status}) em {self.data} {self.hora}"

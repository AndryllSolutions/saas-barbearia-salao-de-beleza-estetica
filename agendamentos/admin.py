from django.contrib import admin
from .models import Agendamento, Cliente, Servico

@admin.register(Agendamento)
class AgendamentoAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'servico', 'usuario', 'data', 'hora', 'criado_em')
    readonly_fields = ('criado_em',)  # só leitura no formulário

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'telefone')

@admin.register(Servico)
class ServicoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'preco')

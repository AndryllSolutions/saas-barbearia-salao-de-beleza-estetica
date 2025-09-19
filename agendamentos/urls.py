from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('novo/', views.novo_agendamento, name='novo_agendamento'),
    path('editar/<int:id>/', views.editar_agendamento, name='editar_agendamento'),
    path('excluir/<int:id>/', views.excluir_agendamento, name='excluir_agendamento'),
    path("meus/", views.meus_agendamentos, name="meus_agendamentos"),

]

# 💈 SaaS - Sistema de Agendamento para Barbearia, Salão de Beleza e Estética

Este projeto é um **SaaS de agendamento** desenvolvido em **Django (Python)**, voltado para barbearias, salões de beleza e clínicas de estética.  
O sistema permite que clientes agendem serviços online, enquanto administradores e funcionários têm acesso a ferramentas de gestão.

---

## 🚀 Funcionalidades

- Autenticação de usuários (**cliente, funcionário e administrador**)
- Cadastro e gestão de **serviços**
- Cadastro de **clientes** (com ou sem vínculo a usuário do sistema)
- Criação, edição e exclusão de **agendamentos**
- Diferentes **níveis de acesso** (admin, funcionário, cliente)
- Dashboard para acompanhar status dos agendamentos
- Páginas de listagem para cada tipo de usuário:
  - Cliente → "Meus Agendamentos"
  - Funcionário → Agendamentos gerais
  - Administrador → Painel completo com filtros

---

## 🛠️ Tecnologias utilizadas

- **Python 3.13**
- **Django 5.2**
- **SQLite** (banco de dados local, fácil de trocar por PostgreSQL/MySQL)
- **Bootstrap** (para os templates HTML)

---

## 📦 Como rodar o projeto

1. Clone este repositório:

```bash
git clone https://github.com/AndryllSolutions/saas-barbearia-salao-de-beleza-estetica.git
cd saas-barbearia-salao-de-beleza-estetica

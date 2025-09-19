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
Crie e ative um ambiente virtual:

bash
Copiar código
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
.venv\Scripts\activate     # Windows
Instale as dependências:

bash
Copiar código
pip install -r requirements.txt
Rode as migrações e crie o banco:

bash
Copiar código
python manage.py migrate
Crie um superusuário (admin):

bash
Copiar código
python manage.py createsuperuser
Inicie o servidor local:

bash
Copiar código
python manage.py runserver
👤 Acessos
Admin → Painel administrativo e dashboard completo

Funcionário → Pode cadastrar, editar e gerenciar agendamentos

Cliente → Pode visualizar e gerenciar apenas seus agendamentos

📌 Estrutura do projeto
bash
Copiar código
.
├── agendamentos/      # App responsável por clientes, serviços e agendamentos
├── users/             # App de autenticação e controle de papéis (roles)
├── templates/         # Templates HTML
├── core/              # Configuração principal do Django
├── db.sqlite3         # Banco de dados local (ignorado no git)
├── manage.py
└── README.md
📝 Licença
Este projeto é open-source, desenvolvido por Andryll Solutions ⚡

yaml
Copiar código

---

👉 Quer que eu já prepare também o `requirements.txt` com as libs principais (`django`, `python-dotenv`, etc.) pra subir junto?





Perguntar ao ChatGPT

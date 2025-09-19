from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # autenticação
    path('accounts/login/', auth_views.LoginView.as_view(
        template_name='registration/login.html'
    ), name='login'),

    path('accounts/logout/', auth_views.LogoutView.as_view(
        next_page='/'
    ), name='logout'),

    path('accounts/register/', user_views.register, name='register'),

    # apps
    path('', include('agendamentos.urls')),

    # painel/admin custom
    path("dashboard/", user_views.dashboard, name="dashboard"),
    path("usuarios/", user_views.gerenciar_usuarios, name="gerenciar_usuarios"),
]

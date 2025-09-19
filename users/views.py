from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group



def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Adiciona no grupo "Cliente" por padrão
            grupo_cliente = Group.objects.get(name="Cliente")
            user.groups.add(grupo_cliente)
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "registration/register.html", {"form": form})



@login_required
def dashboard(request):
    return render(request, "dashboard.html")


from django.contrib.auth.decorators import user_passes_test

def is_admin(user):
    return user.groups.filter(name="Admin").exists()

@user_passes_test(is_admin)
def gerenciar_usuarios(request):
    return render(request, "usuarios/lista.html")
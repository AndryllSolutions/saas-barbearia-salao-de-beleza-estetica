from django.shortcuts import render, redirect, get_object_or_404
from .models import Agendamento, Cliente, Servico
from django.contrib.auth.decorators import login_required
from .models import Agendamento
from users.decorators import role_required
from users.decorators import role_required
from .models import Agendamento, Cliente, Servico
from users.models import User

@login_required
def home(request):
    agendamentos = Agendamento.objects.all().order_by('-criado_em')
    return render(request, 'agendamentos/home.html', {'agendamentos': agendamentos})


from django.contrib.auth.decorators import login_required

@login_required
@role_required("admin", "funcionario", "cliente")
def novo_agendamento(request):
    if request.method == "POST":
        servico_id = request.POST.get("servico")
        data = request.POST["data"]
        hora = request.POST["hora"]

        # 🔥 se funcionário selecionou um cliente já existente
        usuario_cliente_id = request.POST.get("cliente_usuario")

        if usuario_cliente_id:
            usuario_cliente = User.objects.get(id=usuario_cliente_id)
            cliente, _ = Cliente.objects.get_or_create(
                usuario=usuario_cliente,
                defaults={
                    "nome": usuario_cliente.username,
                    "telefone": "",
                }
            )
        else:
            # 🔥 cria cliente novo sem login
            cliente_nome = request.POST["nome"]
            cliente_tel = request.POST["telefone"]
            cliente, _ = Cliente.objects.get_or_create(
                nome=cliente_nome,
                telefone=cliente_tel
            )

        servico = Servico.objects.get(id=servico_id)

        Agendamento.objects.create(
            cliente=cliente,
            servico=servico,
            data=data,
            hora=hora,
            usuario=request.user  # quem cadastrou (funcionário/admin)
        )
        return redirect("home")

    servicos = Servico.objects.all()
    usuarios_clientes = User.objects.filter(role="cliente")
    return render(request, "agendamentos/novo.html", {
        "servicos": servicos,
        "usuarios_clientes": usuarios_clientes
    })

@login_required
@role_required("admin", "funcionario", "cliente")
def editar_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)
  # 🔥 Cliente só pode editar o que é dele
    if request.user.is_cliente() and agendamento.usuario != request.user:
        return redirect("home")
    
    if request.method == "POST":
        cliente_nome = request.POST["nome"]
        cliente_tel = request.POST["telefone"]
        servico_id = request.POST["servico"]
        data = request.POST.get("data") or agendamento.data
        hora = request.POST.get("hora") or agendamento.hora

        cliente, _ = Cliente.objects.get_or_create(
            nome=cliente_nome, telefone=cliente_tel
        )
        servico = Servico.objects.get(id=servico_id)

        agendamento.cliente = cliente
        agendamento.servico = servico
        agendamento.data = data
        agendamento.hora = hora
 # 🔥 controle de status
        if request.user.role == "admin":
            agendamento.status = request.POST.get("status", agendamento.status)
        elif request.user.role == "funcionario":
            novo_status = request.POST.get("status")
            if novo_status in ["confirmado", "concluido"]:
                agendamento.status = novo_status
        # 🔥 Só admin ou funcionário podem alterar o status
        if request.user.is_admin() or request.user.is_funcionario():
            agendamento.status = request.POST.get("status", agendamento.status)

        agendamento.save()
        return redirect("home")

    servicos = Servico.objects.all()
    return render(
        request,
        "agendamentos/editar.html",
        {"agendamento": agendamento, "servicos": servicos},
    )

@login_required
@role_required("admin")
def excluir_agendamento(request, id):
    agendamento = get_object_or_404(Agendamento, id=id)

    if request.method == 'POST':
        agendamento.delete()
        return redirect('home')

    return render(request, 'agendamentos/excluir.html', {'agendamento': agendamento})


@login_required
@login_required
@role_required("admin", "cliente")
def meus_agendamentos(request):
    if request.user.role == "cliente":
        # pega o perfil cliente vinculado a esse user
        cliente = getattr(request.user, "perfil_cliente", None)
        if cliente:
            agendamentos = Agendamento.objects.filter(cliente=cliente)
        else:
            agendamentos = Agendamento.objects.none()  # não tem cliente vinculado
    else:
        # admin pode ver todos
        agendamentos = Agendamento.objects.all()

    return render(request, "agendamentos/lista.html", {"agendamentos": agendamentos})





@login_required
@role_required("admin")
def dashboard(request):
    agendamentos = Agendamento.objects.all()

    # 🔥 filtro por status
    status = request.GET.get("status")
    if status:
        agendamentos = agendamentos.filter(status=status)

    return render(request, "dashboard.html", {
        "agendamentos": agendamentos,
        "status_selecionado": status
    })

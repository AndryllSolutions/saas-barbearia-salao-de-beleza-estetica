from django.core.exceptions import PermissionDenied

def role_required(*roles):
    """
    Verifica se o usuário tem um dos papéis permitidos.
    Exemplo: @role_required("admin", "funcionario")
    """
    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                raise PermissionDenied
            if request.user.role not in roles:
                raise PermissionDenied
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator

from rest_framework.permissions import BasePermission

class IsActiveUser(BasePermission):
    """
    Разрешение, которое проверяет, является ли пользователь активным.
    """
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_active)

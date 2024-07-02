from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Позволяет только владельцу объекта редактировать его.
    """
    def has_object_permission(self, request, view, obj):
        # Разрешить GET, HEAD, OPTIONS запросы без проверки прав
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверяем, что пользователь авторизован и это его собственный профиль
        return obj == request.user

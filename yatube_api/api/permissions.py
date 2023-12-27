from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Предоставляет доступ на изменение или удаление только автору поста.
    В ином случае доступ только для чтения.
    """
    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )

from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.exceptions import PermissionDenied

from posts.models import Post, Group
from .serializers import PostSerializer, GroupSerializer, CommentSerializer


def get_post(self):
    """Получает объект поста."""
    return get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для объектов модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        """Создает запись, в которой автором является текущий пользователь."""
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        """Проверяет, что только автор поста может его изменить."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Проверяет, что только автор поста может его удалить."""
        if instance.author != self.request.user:
            raise PermissionDenied('Удаление чужого контента запрещено!')
        instance.delete()


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для объектов модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для объектов модели Comment."""
    serializer_class = CommentSerializer

    def get_queryset(self):
        """Возвращает queryset c комментариями к текущей записи."""
        return get_post(self).comments.all()

    def perform_create(self, serializer):
        """
        Создает комментарий, в котором автором является текущий пользователь.
        """
        serializer.save(
            author=self.request.user,
            post=get_post(self)
        )

    def perform_update(self, serializer):
        """Проверяет, что только автор комментария может его изменить."""
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, instance):
        """Проверяет, что только автор комментария может его изменить."""
        if instance.author != self.request.user:
            raise PermissionDenied('Изменение чужого контента запрещено!')
        instance.delete()

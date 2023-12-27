from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import LimitOffsetPagination

from api.permissions import IsAuthorOrReadOnly
from posts.models import Post, Group
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)


def get_post(self):
    """Получает объект поста."""
    return get_object_or_404(Post, pk=self.kwargs.get('post_id'))


class PostViewSet(viewsets.ModelViewSet):
    """ViewSet для объектов модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,
    )
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        """Создает запись, в которой автором является текущий пользователь."""
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для объектов модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    """ViewSet для объектов модели Comment."""
    serializer_class = CommentSerializer
    permission_classes = (
        permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly,
    )

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


class FollowViewSet(viewsets.ModelViewSet):
    """ViewSet для объектов модели Follow."""
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        """Возвращает queryset c подписками для текущего пользователя."""
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        """
        Создает подписку, в которой подписчиком является текущий пользователь.
        """
        serializer.save(user=self.request.user)

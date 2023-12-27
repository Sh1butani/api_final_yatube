from django.shortcuts import get_object_or_404
from rest_framework import viewsets, permissions, filters, mixins

from posts.models import Post, Group
from .serializers import (
    PostSerializer, GroupSerializer, CommentSerializer, FollowSerializer
)
from .viewsets import BasePostAuthorViewSet, BaseCommentAuthorViewSet


class PostViewSet(BasePostAuthorViewSet):
    """ViewSet для объектов модели Post."""
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    """ViewSet для объектов модели Group."""
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.AllowAny,)


class CommentViewSet(BaseCommentAuthorViewSet):
    """ViewSet для объектов модели Comment."""
    serializer_class = CommentSerializer


class FollowViewSet(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
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

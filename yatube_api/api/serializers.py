from rest_framework import serializers

from posts.models import Comment, Follow, Group, Post


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Post"""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Post
        fields = (
            'id', 'text', 'author', 'image', 'group', 'pub_date',
        )


class GroupSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Group"""
    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Comment"""
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'text', 'created', 'post')
        read_only_fields = ('post',)


class FollowSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Follow"""
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Follow
        fields = ('user', 'following',)

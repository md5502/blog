from djoser.serializers import UserCreateSerializer
from django.contrib.auth import get_user_model

from blog.models import Comment, Post, Category
from rest_framework.serializers import ModelSerializer, SerializerMethodField, HyperlinkedIdentityField

User = get_user_model()
class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ['id', 'email', 'name', 'password']


class PostListSerializer(ModelSerializer):
    dietale_url = HyperlinkedIdentityField(
        view_name='api:Post_detail'
    )
    author = SerializerMethodField()

    class Meta:
        model = Post
        fields = [
            'title',
            'author',
            'lead',
            'dietale_url',
        ]

    def get_author(self, obj):
        return obj.author.name

class PostDietaleSerializer(ModelSerializer):
    comments = SerializerMethodField()
    comment_count = SerializerMethodField()

    class Meta:
        model = Post
        fields = "__all__"

    def get_comments(self, obj):
        post_id = obj.id
        qs = Comment.objects.filter(post_id=post_id)
        comments = CommentSerializer(qs, many=True).data
        return comments

    def get_comment_count(self, obj):
        post_id = obj.id
        comments_count = len(Comment.objects.filter(post_id=post_id).values())
        return comments_count

class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"


class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
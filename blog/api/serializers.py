from rest_framework.serializers import ModelSerializer

from .models import Post, Comment


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'
        read_only_fields = ['user', ]


class CommentSerializer(ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user', ]

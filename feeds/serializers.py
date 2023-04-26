from rest_framework import serializers
from .models import Post, PostComment, PostLike

class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('__all__')

class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    pub_date = serializers.DateTimeField(label='Published Date', read_only=True)
    updated = serializers.DateTimeField(label='Updated Date', read_only=True)
    
    class Meta:
        model = Post
        fields = ['id', 'user_id', 'title',
                  'body', 'image', 'pub_date', 'updated']


class PostCommentSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    pub_date = serializers.DateTimeField(label='Published Date', read_only=True)
    updated = serializers.DateTimeField(label='Updated Date', read_only=True)

    class Meta:
        model = PostComment
        fields = ['id', 'post_id', 'user_id', 'comment', 'pub_date', 'updated']


class PostLikeSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(label='ID', read_only=True)

    class Meta:
        model = PostLike
        fields = ['id', 'post_id', 'user_id']

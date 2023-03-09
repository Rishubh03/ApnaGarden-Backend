from django.shortcuts import render
from .serializers import PostSerializer, PostCommentSerializer, PostLikeSerializer, PostCreateSerializer
from django.http import Http404
from rest_framework.views import APIView
from account.models import User
from rest_framework.response import Response
from rest_framework import status
from .models import Post, PostComment, PostLike
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
# Create your views here.

class PostCreate(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		request.data['user_id'] = request.user.id
		request.data['slug'] = request.data['title'].replace(' ', '-').lower()
		serializer = PostCreateSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user_id=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostList(APIView):
	"""
	List all posts, or create a new post.
	"""
	permission_classes = (IsAuthenticatedOrReadOnly,)
	def get(self, request, format=None):
		posts = Post.objects.all()
		serializer = PostSerializer(posts, many=True)
		return Response(serializer.data)

class PostDetail(APIView):
	"""
	Retrieve, update or delete a post instance.
	"""
	permission_classes = (IsAuthenticated,)
	def get_object(self, pk):
		try:
			return Post.objects.get(pk=pk)
		except Post.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer = PostSerializer(post)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		post = self.get_object(pk)
		serializer = PostSerializer(post, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		post = self.get_object(pk)
		post.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostCommentCreate(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		serializer = PostCommentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user_id=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostCommentList(APIView):
	"""
	List all comments, or create a new comment.
	"""
	def get(self, request, format=None):
		comments = PostComment.objects.all()
		serializer = PostCommentSerializer(comments, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):
		serializer = PostCommentSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostCommentDetail(APIView):
	"""
	Retrieve, update or delete a comment instance.
	"""
	def get_object(self, pk):
		try:
			return PostComment.objects.get(pk=pk)
		except PostComment.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		comment = self.get_object(pk)
		serializer = PostCommentSerializer(comment)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		comment = self.get_object(pk)
		serializer = PostCommentSerializer(comment, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		comment = self.get_object(pk)
		comment.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostLikeCreate(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request, format=None):
		serializer = PostLikeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save(user_id=request.user)
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostLikeList(APIView):
	"""
	List all likes, or create a new like.
	"""
	def get(self, request, format=None):
		likes = PostLike.objects.all()
		serializer = PostLikeSerializer(likes, many=True)
		return Response(serializer.data)

class PostLikeDetail(APIView):
	"""
	Retrieve, update or delete a like instance.
	"""
	def get_object(self, pk):
		try:
			return PostLike.objects.get(pk=pk)
		except PostLike.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		like = self.get_object(pk)
		serializer = PostLikeSerializer(like)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		like = self.get_object(pk)
		serializer = PostLikeSerializer(like, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		like = self.get_object(pk)
		like.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)

class PostLikeCount(APIView):
	def get(self, request, pk,format=None):
		likes = PostLike.countLikes(PostLike,pk)
		payload = {'likes': likes}
		return Response(payload)	

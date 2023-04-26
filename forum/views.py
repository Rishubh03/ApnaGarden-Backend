from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from account.models import User
from rest_framework.response import Response
from rest_framework import status
from .serializers import ForumSerializer, ThreadSerializer, ThreadPostSerializer
from .models import Forum, Thread, ThreadPost
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)
# Create your views here.


class ForumView(APIView):
	permission_classes = (IsAuthenticated,)
	def get(self, request, format=None):
		forum = Forum.objects.all()
		serializer = ForumSerializer(forum, many=True)
		return Response(serializer.data)


class ForumDetail(APIView):
	permission_classes = (IsAuthenticated,)
	def get_object(self, pk):
		try:
			return Forum.objects.get(pk=pk)
		except Forum.DoesNotExist:
			raise Http404
		
	def get(self, request, pk, format=None):
		forum = self.get_object(pk)
		serializer = ForumSerializer(forum)
		return Response(serializer.data)


class ThreadView(APIView):
	permission_classes = (IsAuthenticated,)
	def get_object(self, fk):
		try:
			return Thread.objects.filter(forum=fk)
		except Thread.DoesNotExist:
			raise Http404

	def get(self, request, fk,format=None):
		thread = self.get_object(fk)
		serializer = ThreadSerializer(thread, many=True)
		return Response(serializer.data)


class ThreadDetail(APIView):
	permission_classes = (IsAuthenticated,)
	def get_object(self, pk):
		try:
			return Thread.objects.get(pk=pk)
		except Thread.DoesNotExist:
			raise Http404

	def get(self, request, pk, format=None):
		thread = self.get_object(pk)
		serializer = ThreadSerializer(thread)
		return Response(serializer.data)

	def put(self, request, pk, format=None):
		thread = self.get_object(pk)
		serializer = ThreadSerializer(thread, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):
		thread = self.get_object(pk)
		thread.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
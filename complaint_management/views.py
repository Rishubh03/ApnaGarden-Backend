from django.http import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from account.models import User
from .models import Complaint, Feedback
from .serializers import ComplaintSerializer, FeedbackSerializer, ComplaintCreateSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


class CreateComplaint(APIView):
    """
    
    """
    permission_classes = [IsAuthenticated]    

    def post(self, request, format=None):
        request.data['user_id'] = request.user.id
        serializer = ComplaintCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ComplaintList(APIView):
    """
    
    """    
    def get(self, request, format=None):
        user = User.objects.get(id = request.user.id)
        complaint = Complaint.objects.filter(user_id = user)
        serializer = ComplaintSerializer(complaint, many=True)
        return Response(serializer.data)
    

    def post(self, request, format=None):
        user = User.objects.get(id = request.user.id)
        request.data['user_id'] = request.user.id
        serializer = ComplaintSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

class ComplaintDetail(APIView):
    
    permission_classes = [IsAuthenticated]
    
    def get_object(self, pk):
        try:
            return Complaint.objects.get(pk=pk)
        except Complaint.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        complaint = self.get_object(pk)
        serializer = ComplaintSerializer(complaint, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, pk, format=None):
        complaint = self.get_object(pk)
        complaint.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class FeedbackList(APIView):
    """
    
    """
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        user = User.objects.get(id = request.user)
        feedback = Feedback.objects.filter(user_id = user)
        serializer = ComplaintSerializer(feedback, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = FeedbackSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

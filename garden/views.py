from django.http import Http404
from rest_framework.views import APIView
from .models import Ward, Garden, Ratings
from .serializers import WardSerializer, GardenSerializer, RatingSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.parsers import MultiPartParser, FormParser


class GardenList(APIView):
	"""

  	"""
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	def get(self,request,format=None):
		garden = Garden.objects.all()
		serializer = GardenSerializer(garden,many = True)
		return Response(serializer.data)
	
class GardenCreate(APIView):
	parser_classes = (MultiPartParser, FormParser)
	permission_classes = [permissions.IsAuthenticated]
	def post(self,request, format = None):
		serializer = GardenSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class GardenDetail(APIView):
	parser_classes = (MultiPartParser, FormParser)
	permission_classes = [permissions.IsAuthenticated]
	def get_object(self, pk):
		try:
			return Garden.objects.get(pk=pk)
		except Garden.DoesNotExist:
			raise Http404
		
	def put(self,pk, request, format=None):
		garden = self.get_object(pk)
		serializer = GardenSerializer(garden, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self,pk, request, format=None):
		garden = self.get_object(pk)
		garden.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	def get(self, pk, request, format=None):
		garden = self.get_object(pk)
		serializer = GardenSerializer(garden)
		return Response(serializer.data)
	
class WardList(APIView):
	"""

  	"""
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
	def get(self,request,format=None):
		ward = Ward.objects.all()
		serializer = WardSerializer(ward,many = True)
		return Response(serializer.data)

class WardCreate(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def post(self,request, format = None):
		serializer = WardSerializer(data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
class WardDetail(APIView):
	permission_classes = [permissions.IsAuthenticated]
	def get_object(self, pk):
		try:
			return Ward.objects.get(pk=pk)
		except Ward.DoesNotExist:
			raise Http404
		
	def put(self,pk, request, format=None):
		ward = self.get_object(pk)
		serializer = WardSerializer(ward, data = request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
	
	def delete(self,pk, request, format=None):
		ward = self.get_object(pk)
		ward.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
	
	def get(self, pk, request, format=None):
		ward = self.get_object(pk)
		serializer = WardSerializer(ward)
		return Response(serializer.data)
	
class RatingTotal(APIView):
	def get(self,request,garden_id,format=None):
		print(garden_id)
		rating = Ratings.calculate_rating(garden_id= garden_id)
		if rating is not None:
			payload = {'rating': rating}
			return Response(payload, status=status.HTTP_200_OK)
		else:
			payload = {'rating': 0}
			return Response(payload, status=status.HTTP_200_OK)
		
class RatingList(APIView):
	def get(self,request,garden_id,format=None):
		rating = Ratings.objects.filter(garden_id = garden_id)
		serializer = RatingSerializer(rating,many = True)
		return Response(serializer.data)
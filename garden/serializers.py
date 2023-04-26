from dataclasses import field
from django.db.models import fields
from rest_framework import serializers
from .models import Garden, Ward, Ratings

                
class WardSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        class Meta:
                model = Ward
                fields = ('__all__')

class GardenSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        image_url = serializers.ImageField(required=False)
        class Meta:
                model = Garden
                fields = ('__all__')

class RatingSerializer(serializers.ModelSerializer):
        id = serializers.IntegerField(read_only=True)
        user_id = serializers.CharField(source='user_id.firstname',)
        class Meta:
                model = Ratings
                fields = ('__all__')
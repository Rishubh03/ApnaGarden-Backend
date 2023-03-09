from rest_framework import serializers
from .models import Complaint, Feedback

class ComplaintCreateSerializer(serializers.ModelSerializer):
        class Meta:
                model = Complaint
                fields = ('__all__')

class ComplaintSerializer(serializers.ModelSerializer):
        garden = serializers.CharField(source='garden.garden_name')
        user_id = serializers.CharField(source='user_id.firstname')
        class Meta:
                model = Complaint
                fields = ('__all__')
                
class FeedbackSerializer(serializers.ModelSerializer):
        class Meta:
                model = Feedback
                fields = ('__all__')
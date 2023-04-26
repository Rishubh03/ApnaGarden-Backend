from rest_framework import serializers
from .models import Forum, Thread, ThreadPost

class ForumSerializer(serializers.ModelSerializer):
	class Meta:
		model = Forum
		fields = ('__all__')

class ThreadSerializer(serializers.ModelSerializer):
	class Meta:
		model = Thread
		fields = ('__all__')

class ThreadPostSerializer(serializers.ModelSerializer):
	class Meta:
		model = ThreadPost
		fields = ('__all__')
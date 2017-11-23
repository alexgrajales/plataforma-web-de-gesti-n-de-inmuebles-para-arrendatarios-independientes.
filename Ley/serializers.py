from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Ley.models import Ley

class LeySerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Ley
		fields = '__all__'
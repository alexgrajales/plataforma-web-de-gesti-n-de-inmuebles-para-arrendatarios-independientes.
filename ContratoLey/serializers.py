from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from ContratoLey.models import ContratoLey

class ContratoLeySerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = ContratoLey
		fields = '__all__'
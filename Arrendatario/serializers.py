from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Arrendatario.models import Arrendatario

class ArrendatarioSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Arrendatario
		fields = '__all__'
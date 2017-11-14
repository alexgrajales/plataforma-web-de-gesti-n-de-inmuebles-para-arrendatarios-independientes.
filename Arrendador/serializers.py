from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Arrendador.models import Arrendador

class ArrendadorSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Arrendador
		fields = '__all__'
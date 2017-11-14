from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Archivo.models import Archivo

class ArchivoSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Archivo
		fields = '__all__'
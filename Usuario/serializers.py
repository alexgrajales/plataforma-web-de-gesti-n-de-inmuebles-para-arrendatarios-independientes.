from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Usuario.models import Usuario
from  Archivo.serializers import ArchivoSerializer

class UsuarioSerializer(mongoserializers.DocumentSerializer):
	archivos = ArchivoSerializer(read_only=True, many=True)

	class Meta:
		model = Usuario
		fields = '__all__'
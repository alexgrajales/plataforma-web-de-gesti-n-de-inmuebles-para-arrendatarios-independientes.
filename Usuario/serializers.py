from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Usuario.models import Usuario
class UsuarioSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Usuario
		fields = '__all__'
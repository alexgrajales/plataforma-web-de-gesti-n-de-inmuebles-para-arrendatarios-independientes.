from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Administrador.models import Administrador


class AdministradorSerializer(mongoserializers.DocumentSerializer):


	class Meta:
		model = Administrador
		fields = '__all__'
from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Contrato.models import Contrato

class ContratoSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Contrato
		fields = '__all__'
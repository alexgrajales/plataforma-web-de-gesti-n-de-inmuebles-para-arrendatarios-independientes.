from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Pago.models import Pago

class PagoSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Pago
		fields = '__all__'
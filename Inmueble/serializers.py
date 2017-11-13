from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Inmueble.models import Inmueble
class InmuebleSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Inmueble
		fields = '__all__'
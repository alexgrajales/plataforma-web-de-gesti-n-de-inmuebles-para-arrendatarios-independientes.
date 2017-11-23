from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Habitacion.models import Habitacion

class HabitacionSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Habitacion
		fields = '__all__'
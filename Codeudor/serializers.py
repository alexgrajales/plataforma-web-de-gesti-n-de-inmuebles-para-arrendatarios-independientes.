from rest_framework import serializers
from rest_framework_mongoengine import serializers as mongoserializers
from Codeudor.models import Codeudor

class CodeudorSerializer(mongoserializers.DocumentSerializer):
	class Meta:
		model = Codeudor
		fields = '__all__'
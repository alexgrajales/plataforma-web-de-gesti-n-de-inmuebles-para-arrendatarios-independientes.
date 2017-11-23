from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Habitacion.serializers import *
from Habitacion.models import Habitacion


class HabitacionViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = HabitacionSerializer
	def get_queryset(self):
		return Habitacion.objects.all()
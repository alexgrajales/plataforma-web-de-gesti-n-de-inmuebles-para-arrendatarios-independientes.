from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Arrendador.serializers import *
from Arrendador.models import Arrendador


class ArrendadorViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = ArrendadorSerializer
	def get_queryset(self):
		return Arrendador.objects.all()
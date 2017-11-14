from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Archivo.serializers import *
from Archivo.models import Archivo


class ArchivoViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = ArchivoSerializer
	def get_queryset(self):
		return Archivo.objects.all()
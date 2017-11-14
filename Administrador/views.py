from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Administrador.serializers import *
from Administrador.models import Administrador


class AdministradorViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = AdministradorSerializer
	def get_queryset(self):
		return Administrador.objects.all()
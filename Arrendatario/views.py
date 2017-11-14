from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Arrendatario.serializers import *
from Arrendatario.models import Arrendatario


class ArrendatarioViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = ArrendatarioSerializer
	def get_queryset(self):
		return Arrendatario.objects.all()
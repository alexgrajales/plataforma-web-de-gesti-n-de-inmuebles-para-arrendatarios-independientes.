from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Contrato.serializers import *
from Contrato.models import Contrato


class ContratoViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = ContratoSerializer
	def get_queryset(self):
		return Contrato.objects.all()
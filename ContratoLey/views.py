from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from ContratoLey.serializers import *
from ContratoLey.models import ContratoLey


class ContratoLeyViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = ContratoLeySerializer
	def get_queryset(self):
		return ContratoLey.objects.all()
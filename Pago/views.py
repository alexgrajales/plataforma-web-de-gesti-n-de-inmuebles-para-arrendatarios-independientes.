from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Pago.serializers import *
from Pago.models import Pago


class PagoViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = PagoSerializer
	def get_queryset(self):
		return Pago.objects.all()
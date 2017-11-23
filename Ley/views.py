from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Ley.serializers import *
from Ley.models import Ley


class LeyViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = LeySerializer
	def get_queryset(self):
		return Ley.objects.all()
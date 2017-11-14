from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Codeudor.serializers import *
from Codeudor.models import Codeudor


class CodeudorViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = CodeudorSerializer
	def get_queryset(self):
		return Codeudor.objects.all()
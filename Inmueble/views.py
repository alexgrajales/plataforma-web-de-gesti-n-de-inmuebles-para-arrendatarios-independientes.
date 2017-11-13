from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Inmueble.serializers import *
from Inmueble.models import Inmueble
#
# def index_view(request):
# 	context = {}
# 	return TemplateResponse(request, 'index.html', context)

class InmuebleViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = InmuebleSerializer
	def get_queryset(self):
		return Inmueble.objects.all()
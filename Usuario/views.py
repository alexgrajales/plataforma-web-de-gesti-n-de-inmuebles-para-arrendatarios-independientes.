from __future__ import unicode_literals
from django.template.response import TemplateResponse
from rest_framework_mongoengine.viewsets import ModelViewSet as MongoModelViewSet
from Usuario.serializers import *
from Usuario.models import Usuario

def index_view(request):
	context = {}
	return TemplateResponse(request, 'index.html', context)

class UsuarioViewSet(MongoModelViewSet):
	lookup_field = 'id'
	serializer_class = UsuarioSerializer
	def get_queryset(self):
		return Usuario.objects.all()
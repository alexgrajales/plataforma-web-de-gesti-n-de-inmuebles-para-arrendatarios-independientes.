from mongoengine import Document, EmbeddedDocument, fields
from Usuario.models import Usuario

class Arrendatario(Usuario):
    propietario = fields.BooleanField()

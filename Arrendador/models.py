from mongoengine import Document, EmbeddedDocument, fields
from Usuario.models import Usuario

class Arrendador(Usuario):
    contratoLaboral = fields.BooleanField()

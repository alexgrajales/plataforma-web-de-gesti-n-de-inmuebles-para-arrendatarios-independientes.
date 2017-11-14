from mongoengine import Document, EmbeddedDocument, fields
from Usuario.models import Usuario

class Administrador(Usuario):
    superUsuario = fields.BooleanField()


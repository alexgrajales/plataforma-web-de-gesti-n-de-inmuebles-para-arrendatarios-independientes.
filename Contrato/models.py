from mongoengine import Document, EmbeddedDocument, fields
from Arrendador.models import Arrendador
from Arrendatario.models import Arrendatario
from Archivo.models import Archivo


class Contrato(Document):
    archivo = fields.ListField(fields.ReferenceField(Archivo))
    fechainicio = fields.DateTimeField()
    fechafin = fields.DateTimeField()
    estado = fields.IntField()

    def __str__(self):
        return self.archivo
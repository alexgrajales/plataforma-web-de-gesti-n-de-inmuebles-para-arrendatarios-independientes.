from mongoengine import Document, EmbeddedDocument, fields
from Contrato.models import Contrato
from Ley.models import Ley
from Archivo.models import Archivo


class ContratoLey(Document):
    contrato = fields.ListField(fields.ReferenceField(Contrato))
    ley = fields.ListField(fields.ReferenceField(Ley))
    archivo = fields.ListField(fields.ReferenceField(Archivo))
    detalle = fields.StringField()

    def __str__(self):
        return self.contrato
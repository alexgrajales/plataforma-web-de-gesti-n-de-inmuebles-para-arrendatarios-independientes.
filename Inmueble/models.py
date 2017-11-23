from mongoengine import Document, EmbeddedDocument, fields
from Arrendador.models import Arrendador
from Arrendatario.models import Arrendatario
from Archivo.models import Archivo


class Inmueble(Document):
    area = fields.FloatField()
    propiedadRaiz = fields.BooleanField()
    arrendador = fields.ListField(fields.ReferenceField(Arrendador))
    arrendatario = fields.ListField(fields.ReferenceField(Arrendatario))
    archivo = fields.ListField(fields.ReferenceField(Archivo))
    banoscomunes = fields.IntField()
    comedor = fields.BooleanField()
    direccion = fields.StringField()
    estrato = fields.IntField()
    habitaciones = fields.IntField()
    lavadero = fields.IntField()
    parqueadero = fields.BooleanField()
    patio = fields.BooleanField()
    precio = fields.FloatField()
    sala = fields.BooleanField()
    salacomedor = fields.BooleanField()
    telefono = fields.StringField()
    tipo = fields.StringField()
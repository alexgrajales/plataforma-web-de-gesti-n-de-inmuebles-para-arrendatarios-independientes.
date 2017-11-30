from mongoengine import Document, EmbeddedDocument, fields
from Arrendador.models import Arrendador
from Arrendatario.models import Arrendatario
from Archivo.models import Archivo
from Inmueble.models import Inmueble


class Pago(Document):
    archivo = fields.ListField(fields.ReferenceField(Archivo))
    arrendatario = fields.ListField(fields.ReferenceField(Arrendatario))
    inmueble = fields.ListField(fields.ReferenceField(Inmueble))
    fecha = fields.DateTimeField()
    descripcionpago = fields.StringField()
    descripcionaprobacion = fields.StringField()
    pagoaprobadoarrendador = fields.BooleanField()

    def __str__(self):
        return self.descripcionpago
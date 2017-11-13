from mongoengine import Document, EmbeddedDocument, fields

class Inmueble(Document):
    area = fields.StringField()
    banosComunes = fields.IntField()
    comedor = fields.StringField()
    direccion = fields.StringField()
    estrato = fields.IntField()
    lavadero = fields.IntField()
    parqueadero = fields.BooleanField()
    patio = fields.BooleanField()
    precio = fields.FloatField()
    sala = fields.BooleanField()
    salaComedor = fields.BooleanField()
    telefono = fields.StringField()
    tipo = fields.StringField()
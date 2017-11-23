from mongoengine import Document, EmbeddedDocument, fields


class Habitacion(Document):
    armario = fields.IntField()
    bano = fields.BooleanField()
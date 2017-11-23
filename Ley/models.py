from mongoengine import Document, EmbeddedDocument, fields


class Ley(Document):
    descripcion = fields.StringField()
    nombreley = fields.StringField()
    referencialey = fields.StringField()
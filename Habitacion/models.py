from mongoengine import Document, EmbeddedDocument, fields


class Habitacion(Document):
    descripcion = fields.StringField()
    armario = fields.IntField()
    bano = fields.BooleanField()

    def __str__(self):
        return self.descripcion
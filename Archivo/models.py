from mongoengine import Document, EmbeddedDocument, fields

class Archivo(Document):
    descripcion = fields.StringField()
    fecha = fields.DateTimeField()
    archivo = fields.FileField()
    tipo = fields.StringField()


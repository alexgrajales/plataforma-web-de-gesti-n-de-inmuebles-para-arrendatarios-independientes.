from mongoengine import Document, EmbeddedDocument, fields
from Archivo.models import Archivo

class Usuario(Document):
    nombre = fields.StringField()
    apellido = fields.StringField()
    cedula = fields.StringField()
    clave = fields.StringField()
    correo = fields.EmailField()
    direccion = fields.StringField()
    edad = fields.IntField()
    telefono = fields.StringField()
    celular = fields.StringField()
    archivo = fields.ListField(fields.ReferenceField(Archivo))
    meta = {'allow_inheritance': True}

    def __str__(self):
        return self.nombre+self.apellido
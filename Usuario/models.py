from mongoengine import Document, EmbeddedDocument, fields

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


# class Libro(Document):
# 	nombre = fields.StringField()
# 	autor = fields.ReferenceField(Autor, dbref=True)

from mongoengine import Document, EmbeddedDocument, fields
from Usuario.models import Usuario

class Codeudor(Usuario):
    contrato = fields.BooleanField()
    propiedadRaiz = fields.BooleanField()

    def __str__(self):
        return "List: {}".format(self.nombre+self.apellido)


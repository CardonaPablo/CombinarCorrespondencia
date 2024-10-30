from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(80), nullable=False)
    apellido1 = db.Column(db.String(80), nullable=False)
    apellido2 = db.Column(db.String(80), nullable=False)
    cargo = db.Column(db.String(80), nullable=False)
    empresa = db.Column(db.String(80), nullable=False)
    calle = db.Column(db.String(80), nullable=False)
    numeroExt = db.Column(db.String(80), nullable=False)
    numeroInt = db.Column(db.String(80), nullable=False)
    colonia = db.Column(db.String(80), nullable=False)
    municipio = db.Column(db.String(80), nullable=False)
    estado = db.Column(db.String(80), nullable=False)
    codigoPostal = db.Column(db.String(80), nullable=False)
    telefono = db.Column(db.String(80), nullable=False)
    correoElectronico = db.Column(db.String(80), nullable=False)
    fechaNacimiento = db.Column(db.String(80), nullable=False)
    edad = db.Column(db.String(80), nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'nombre': self.nombre,
            'apellido1': self.apellido1,
            'apellido2': self.apellido2,
            'cargo': self.cargo,
            'empresa': self.empresa,
            'calle': self.calle,
            'numeroExt': self.numeroExt,
            'numeroInt': self.numeroInt,
            'colonia': self.colonia,
            'municipio': self.municipio,
            'estado': self.estado,
            'codigoPostal': self.codigoPostal,
            'telefono': self.telefono,
            'correoElectronico': self.correoElectronico,
            'fechaNacimiento': self.fechaNacimiento,
            'edad': self.edad
        }

    def __repr__(self):
        return f'<User {self.nombre}>'
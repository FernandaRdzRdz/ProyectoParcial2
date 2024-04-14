from app import db
from sqlalchemy import Column, Integer, String, BigInteger, Date, Time, ForeignKey
from sqlalchemy.orm import relationship

class Persona(db.Model):
    __tablename__ = 'persona'
    
    curp = db.Column(db.String(18), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    paterno = db.Column(db.String(30), nullable=False)
    materno = db.Column(db.String(30), nullable=False)
    telefono = db.Column(db.BigInteger, nullable=False)
    celular = db.Column(db.BigInteger, nullable=False)
    correo = db.Column(db.String(100), nullable=False)

class CatalogoTramitante(db.Model):
    __tablename__ = 'catalogo_tramitante'
    
    id_tramite = db.Column(db.Integer, primary_key=True)
    nom_completo = db.Column(db.String(150))

class CatalogoNivel(db.Model):
    __tablename__ = 'catalogo_nivel'
    
    id_tramite = db.Column(db.Integer, primary_key=True)
    nivel = db.Column(db.String(60))

class CatalogoMunicipio(db.Model):
    __tablename__ = 'catalogo_municipio'
    
    id_tramite = db.Column(db.Integer, primary_key=True)
    municipio = db.Column(db.String(60))

class CatalogoAsunto(db.Model):
    __tablename__ = 'catalogo_asunto'
    
    id_tramite = db.Column(db.Integer, primary_key=True)
    asunto = db.Column(db.String(60))

class Tramite(db.Model):
    __tablename__ = 'tramite'
    
    id_tramite = db.Column(db.Integer, primary_key=True)
    num_turno = db.Column(db.Integer, nullable=False)
    curp = db.Column(db.String(18), db.ForeignKey('persona.curp'), nullable=False)
    hora = db.Column(db.Time, nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(15), default='Pendiente')
    
    persona = db.relationship("Persona", backref="tramites")
    tramitante = db.relationship("CatalogoTramitante", backref="tramites")
    nivel = db.relationship("CatalogoNivel", backref="tramites")
    municipio = db.relationship("CatalogoMunicipio", backref="tramites")
    asunto = db.relationship("CatalogoAsunto", backref="tramites")

class User(db.Model):
    __tablename__ = 'user'
    
    id_user = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(15), nullable=False)
    pwd = db.Column(db.String(15))
    rol = db.Column(db.String(50))

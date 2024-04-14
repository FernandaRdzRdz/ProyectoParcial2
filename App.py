from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config['SECRET_KEY']='Esto es un secreto'
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///C:/ProyectosDAW/ProyectoParcial2/database/turnos.db'

db=SQLAlchemy(app)

# #En esta parte se crea la base de datos, solo se ejecuta una vez
# from modelo import Persona, CatalogoTramitante, CatalogoNivel, CatalogoMunicipio, CatalogoAsunto, Tramite, User
# try:
#     with app.app_context():
#         db.create_all()
# except Exception as e:
#     print("Error creating database tables:", e)

from controlador import *

if __name__=='__main__':
    app.run(debug=True)
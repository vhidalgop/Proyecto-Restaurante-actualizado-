from sqlalchemy.orm import sessionmaker
from sqlalchemy import *
from flask_cors import CORS
from flask import Flask, render_template, request,jsonify
from flask_mysqldb import MySQL
from enum import unique
import flask
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, create_engine


base = declarative_base()           
motor = create_engine("mysql://root:@localhost/base_datos")  

class User(base):
    __tablename__ = "users"
    id = Column(Integer(), primary_key = True)
    nombre =  Column(String(50), nullable = False, unique = True)       #Base de usuarios
    contra =  Column(String(50), nullable = False, unique = False)
    def __str__(self):
        return self.nombre
    


sesion = sessionmaker(motor)                #Alchemy
sesion1 = sesion()              #Alchemy
app = Flask(__name__)       #Inicializamos Flask
CORS(app)



mysql = MySQL(app)

@app.route("/inicio_sesion", methods=["POST","GET"])           #Iniciar sesion
def Inicio_sesion():
    print("entrooooo")
    consulta = sesion1.query(User).filter(
                User.nombre == request.json["user"]
            ).first()
    consulta1 = sesion1.query(User).filter(
                User.contra == request.json["contra"]
                ).first()

    if consulta != None and consulta1 !=None:
        print("funciono")
        response = str(consulta.nombre)
        print(type(response))
        print(response)
        msg={
            "sesion":"verdad",
            "nombre":response,
            "mensaje":"Sesion iniciada"
        }
        return msg
    else:
        mensaje_front={
            "sesion":"falso",
            "mensaje":"Datos erroneos intente de nuevo"
        }
        msg1 = jsonify(mensaje_front)
        return mensaje_front
@app.route("/crear", methods=["POST","GET"])  
def createUser():
    consulta_ruta1 = sesion1.query(User).filter(
        User.nombre == request.json["nombre"],
        User.contra == request.json["contra"]
    ).first()
    print("datos",consulta_ruta1)
    if consulta_ruta1 == None:
        print(request.json)
        sesion1.add(User(nombre = request.json["nombre"], contra = request.json["contra"]))
        sesion1.commit()
        print("posta0")
        msg = {
            "mensaje":"cuenta creada",
            "cuenta":"nueva"
        }
        return msg
    elif consulta_ruta1 !=None:
        msg = {
            "mensaje":"Cuenta existente",
            "cuenta":"existente"
        }
        return msg

if __name__ == '__main__':
    #base.metadata.drop_all(motor)
    #base.metadata.create_all(motor)
    app.run(debug=True)
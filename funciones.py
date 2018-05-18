#SERGIO MARCHENA 16387

from neo4j.v1 import GraphDatabase, basic_auth

#Establece el driver y la sesion de Neo4J
driver = GraphDatabase.driver("bolt:localhost:7474", auth=basic_auth("neo4j", "123"))#AGREGAR USERNAME Y PASSWORD PARA ACCESAR A NE0EJ.
session = driver.session()

#funcion para ingresar un doctor req: Nombre, especializacion y telefono
def ingresoDoctor(nombre,especializacion,telefono):
    session.run("CREATE (a:Doctor {nombre: {nombre}, especializacion: {especializacion},telefono: {telefono}})",
                {"nombre": nombre, "especializacion": especializacion,"telefono":telefono})

#Funcion para crear un paciente req: Nombre, enfermedad y telefono
def ingresoPaciente(nombre,enfermedad,telefono):
    session.run("CREATE (a:Paciente {nombre: {nombre}, enfermedad: {enfermedad},telefono: {telefono}})",
                {"nombre": nombre, "enfermedad": enfermedad,"telefono":telefono})

#Establece la fecha de visita y la medicina recetada a la persona
def visita(telefonoPaciente, nombreDoctor, fecha, medicina):
    session.run ("MATCH (paciente:Paciente)-[:Consulto]->(doctor:Doctor)"
                 "WHERE paciente.telefono = {telefonoPaciente} and doctor.nombre = {nombreDoctor}"
                 "CREATE (paciente)-[:VISITO {fecha: {fecha}}]->(doctor)-[:PRESCRIBIO {medicina: {medicina} }]->(paciente)",
                 {"telefonoPaciente": telefonoPaciente,"nombreDoctor":nombreDoctor,"fecha":fecha,"medicina":medicina})

    print (telefonoPaciente + " " + nombreDoctor + " " + fecha + " "+ medicina)

#Busca a todos los medicos con una especialidad dada
def especialidad(espa):
    resultado = session.run("MATCH (doc:Doctor) WHERE doc.especializacion = {espa}"
                            "RETURN doc.nombre AS name",
                            {"espa":espa})
    for record in resultado:
        print ("Especializacion: " + espa + " " + "Doctor: " + record["name"])

#Funcion que establece relacion entre 2 pacientes
def conoce(persona1,persona2):
    session.run ("MATCH (xuno:Paciente),(xdos:Paciente)"
                 "WHERE xuno.nombre = {persona1} AND xdos.nombre = {persona2}"
                 "CREATE (xuno)-[:CONOCE]->(xdos)",
                 {"persona1":persona1,"persona2":p2ersona})
#Funcion para terminar la sesion
def Salir():
    session.close()

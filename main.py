#SERGIO MARCHENA 16387
#LUIS DELGADO 17187

from funciones import *

print ("Bienvenido")


fin = False
while (fin == False):
    print("")
    print ("1. ingreso de un doctor")
    print ("2. ingreso de un paciente")
    print ("3. ingreso de una visita")
    print ("4. consultar especialidad de un doctor")
    print ("5. ingresar relacion entre personas")
    print ("6. salir")
    opcion = (input("elija su opcion: "))


    if opcion == "1":
        nombre = input("nombre del doctor: ")
        especializacion = input("especializacion del doctor: ")
        telefono = int(input("numero de telefono del doctor: "))
        ingresoDoctor(nombre, especializacion, telefono)
        
    if opcion == "2":
        nombre = input("nombre del paciente: ")
        enfermedad = input("enfermedad del paciente: ")
        telefono = int(input("numero de telefono: "))
        ingresoPaciente(nombre, enfermedad, telefono)

    if opcion == "3":
         paciente = str(input ("nombre del paciente: "))
         telPaciente = str(input("telefono del paciente: "))
         doctor = str(input ("nombre del doctor: "))
         fecha= str(input("fecha de la visita: "))
         medicina = str(input("medicina: "))
         visita(telPaciente, doctor,fecha, medicina)
         
    if opcion == "4":
        espa = input("especialidad a buscar: ")
        espa = str(espa)
        especialidad(espa)
        
    if opcion == "5":
        per1 = input("nombre de una persona 1: ")
        per2 = input("nombre de una persona 2: ")
        conoce (per1, per2)





    respuesta = input("Desea seguir? S/N ")
    while (respuesta != "S" and respuesta != "N"):
        print ("Por favor ingrese uno de los caracteres validos (S o N)")
        respuesta = input("Desea realizar otra accion? S/N")

    if (respuesta == "S"):
        fin == False
    else:
        Salir();
        fin = True
        print ("Gracias por usar este sistema.")







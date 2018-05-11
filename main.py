from funciones import *

print "Bienvenido"


fin = False
while (fin == False):
    print ""
    print "1. ingreso de un doctor"
    print "2. ingreso de un paciente"
    print "3. ingreso de una visita"
    print "4. consultar especialidad de un doctor"
    print "5. ingresar relacion entre personas"
    print "6. salir"
    opcion = int(raw_input("elija su opcion: "))


    if opcion == 1:
        nombre = raw_input("nombre del doctor: ")
        especializacion = raw_input("especializacion del doctor: ")
        telefono = int(raw_input("numero de telefono del doctor: "))
        ingresoDoctor(nombre, especializacion, telefono)
        
    if opcion == 2:
        nombre = raw_input("nombre del paciente: ")
        enfermedad = raw_input("enfermedad del paciente: ")
        telefono = int(raw_input("numero de telefono: "))
        ingresoPaciente(nombre, enfermedad, telefono)

    if opcion == 3:
         paciente = raw_input ("nombre del paciente: ")
         telPaciente = raw_input("telefono del paciente: ")
         doctor = raw_input ("nombre del doctor: ")
         fecha= raw_input("fecha de la visita: ")
         medicina = raw_input("medicina: ")
         visita(telPaciente, doctor,fecha, medicina)
         
    if opcion == 4:
        especialidad = raw_input("especialidad a buscar: ")
        especialidad(especialidad)
        
    if opcion == 5:
        per1 = raw_input("nombre de una persona 1: ")
        per2 = raw_input("nombre de una persona 2: ")
        conoce (per1, per2)





    respuesta = raw_input("Desea seguir? S/N ")
    while (respuesta != "S" and respuesta != "N"):
        print "Por favor ingrese uno de los caracteres validos (S o N)"
        respuesta = raw_input("Desea realizar otra accion? S/N")

    if respuesta == "S":
        fin == False
    else:
        Salir();
        fin = True
        print "Gracias por usar este sistema."









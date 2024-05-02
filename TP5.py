alumnos = {
    "41095372": {
        "Nombre": "TOMAS",
        "Apellido": "FARFAN",
        "Fecha de nacimiento": "13/12/1998",
        "DNI": "41095372",
        "Tutor": "NANCY DIAZ",
        "Notas": [8, 7],
        "Faltas": 1,
        "Amonestaciones": 1
    },
    "41097377": {
        "Nombre": "CAMILA",
        "Apellido": "DIAZ",
        "Fecha de nacimiento": "28/01/1998",
        "DNI": "41097377",
        "Tutor": "MARIA MUSEDA",
        "Notas": [6, 9],
        "Faltas": 0,
        "Amonestaciones": 0
    },
    #
    
}



def buscar():
    print("Ingrese un DNI para verificar")
    while True:
         dni=input("Por favor ingrese un DNI ")
         if dni in alumnos:
             mostrar_alumno(dni)
             break
         else:
             print("Dni no asociado a alumno")
             obtener_datos(dni)
             break
    
    
def ABM_alumnos(dni):
    while True:
        mod=input("Elija que accion realizar ")
        if mod.upper()=="M":
            modificar_alumnos(dni)
            break
        elif mod.upper()=="B":
            eliminar_alumno(dni)
            break
        elif mod.upper()=="S":
            print("Finalizado")
            break
        else:
            print("Elija una opcion valida, escriba (M) para modificar, (B) para eliminar o (S) para salir ")
    
def mostrar_alumno(dni):
    alumno=alumnos[dni]
    print(f"Nombre: {alumno['Nombre']}\n"
          f"Apellido: {alumno['Apellido']}\n"
          f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}\n"
          f"Dni: {alumno['DNI']}\n"
          f"Tutor: {alumno['Tutor']}\n"
          f"Notas: {alumno['Notas']}\n"
          f"Faltas: {alumno['Faltas']}\n"
          f"Amonestaciones: {alumno['Amonestaciones']}")
    print("Dese modificar o eliminar alumno? escriba (M) para modificar, (B) para eliminar o (S) para salir ")
    ABM_alumnos(dni)    
                 
def modificar_alumnos(dni):
    alumno=alumnos[dni]
    print("Que datos desea modificar ? o (S) para volver")
    print("Nombre,Apellido,Fecha de nacimiento,DNI,Tutor,Notas,Faltas o Amonestaciones")
    print("")
    editor=input("Ingrese dato a modificar ")
    print("")
    
    if editor.upper() == "NOMBRE":
        while True:
            nuevo_nombre = input("Ingrese nuevo nombre:   ")
            if not nuevo_nombre.isnumeric():
                break
            else:
                print("Por favor ingrese texto ")
                
        if nuevo_nombre:
            alumno["Nombre"] = nuevo_nombre.upper()
            print("Nuevo nombre es", alumno["Nombre"])
            print("")
            modificar_alumnos(dni)   
        else:
            print("No se ha ingresado un nombre se mantiene el mismo ")
            print("")
            modificar_alumnos(dni)
   
    elif editor.upper() == "APELLIDO":
        while True:
            nuevo_apellido=input("Ingrese nuevo Apellido")
            if not nuevo_apellido.isnumeric():
                break
            else:
                print("Por favor ingrese texto ")
        nuevo_apellido=input("Ingrese nuevo Apellido")
        if nuevo_apellido:
            alumno["Apellido"]= nuevo_apellido.upper()    
            print("El nuevo apelido es ",alumno["Apellido"])  
            print("")  
            modificar_alumnos(dni)
        else:
            print("No se ha ingresado un Apellido se mantiene el mismo")
            print("")
            modificar_alumnos(dni)
                  
    elif editor.upper() == "FECHA DE NACIMIENTO":
        
        new_fecha_nac=input("Ingrese nueva fecha de nacimiento (dd/mm/aaaa): ")
        if new_fecha_nac:
            alumno["Fecha de nacimiento"]= new_fecha_nac.upper()
            print("Nueva fecha de nacimiento ",alumno["Fecha de nacimiento"])
            print("")
            modificar_alumnos(dni)
        else:
            print("No se ha ingresado una fecha se mantiene la misma")
            print("")
            modificar_alumnos(dni)
               
    elif editor.upper() == "DNI": 
        try:
            new_dni=int(input("Ingrese nuevo DNI "))
        except ValueError:
            print("Error por favor ingrese numero enteros /No se modifico dni")
            print("")
            modificar_alumnos(dni)
        if new_dni:
            alumno["DNI"]=new_dni
            print("Nuevo DNI es ",alumno["DNI"])
            print("")
            modificar_alumnos(dni)
                             
    elif editor.upper() == "TUTOR": 
        new_tutor=input("Ingrese el nuevo  nombre del tutor")
        if new_tutor:
            alumno["Tutor"]=new_tutor.upper()
            print("Nombre del tutor es ",new_tutor)
            print("")
            modificar_alumnos(dni)
        else:
            print("No se ha ingresado un tutor se mantiene la misma")
            print("")
            modificar_alumnos(dni)
                
    elif editor.upper() == "NOTAS": 
        new_nota=int(input("Ingrese nueva nota"))
        if new_nota:
            alumno["Notas"].append(new_nota)
            print("Nueva nota asignada",alumno["Notas"])
            print("")
            modificar_alumnos(dni)
        else:
            print("No se asigno nota")
            print("")
            mostrar_alumno(dni)    
        
    elif editor.upper() == "FALTAS": 
        print("Faltas actuales",alumno["Faltas"])
        try:
            new_falta=int(input("Agregar falta "))
        except ValueError:
            print("Error por favor ingrese numero enteros /No se modificaron las faltas")
            print("")
            modificar_alumnos(dni)
        if new_falta:
            alumno["Faltas"]+=new_falta
            print("Se agrego falta, faltas actuales : ",alumno["Faltas"])
            print("")
            modificar_alumnos(dni) 
            
    elif editor.upper() == "AMONESTACIONES": 
        print("Amonestaciones actuales ",alumno["Amonestaciones"])
        try:
            new_amones=int(input("Agregar Amonestacion"))
        except ValueError:
            print("Error por favor ingrese numero enteros /No se modificaron las Amonestaciones")
            print("")
            modificar_alumnos(dni)

        if new_amones:
            alumno["Amonestaciones"]+=new_amones
            print("Se agrego Amonestacion,  Amonestacion actuales : ",alumno["Amonestaciones"])
            print("")
            modificar_alumnos(dni)
                    
    elif editor.upper()=="S":
        print("Atras")
        print("")
        mostrar_alumno(dni)
    else:
        print("Por favor escriba correctamente")
        print("")
        modificar_alumnos(dni)    
               
def obtener_datos(dni):
#Por cuestiones de tiempo no llegue a agregar exception o opciones en caso de que el usuario ingrese algun datoa erroneo como lo hice en "modificar_alumnos"
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        dni = input("Ingrese el DNI del alumno: ")
        fecha_nacimiento = input("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ")
        tutor = input("Ingrese el nombre del tutor del alumno: ")
        nuevo_alumno=carga_datos_alumnos(nombre,apellido,dni,fecha_nacimiento,tutor)
        alumnos[dni]=nuevo_alumno
        mostrar_alumno(dni)
                       
def carga_datos_alumnos(nombre,apellido,dni,fecha_nacimiento,tutor):
        
        dni= {
            "Nombre": nombre,
            "Apellido": apellido,
            "DNI": dni,
            "Fecha de nacimiento": fecha_nacimiento,
            "Tutor": tutor,
            "Notas": [],
            "Faltas": 0,
            "Amonestaciones": 0
        }
    
        return dni

def eliminar_alumno(dni):
    alumno=alumnos[dni]
    print(f"Nombre: {alumno['Nombre']}\n"
          f"Apellido: {alumno['Apellido']}\n"
          f"Fecha de nacimiento: {alumno['Fecha de nacimiento']}\n"
          f"Dni: {alumno['DNI']}\n")
    print("Seguro que desea eliminar?")
    while True:
        validar=input("SI/NO")
        if validar.upper()=="SI":
            del alumnos[dni]
            print("Usuario eliminado correctamente")
            buscar()
            break
        elif validar.upper()=="NO":
            mostrar_alumno(dni)
            break
        else:
            print("Escriba una opcion valida")
            
        
#-------------
#---------------
#
buscar()

        
        


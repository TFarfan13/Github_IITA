import json

archivos_datos_alumnos = "alumnos.txt"

# Cargar los datos del archivo
def cargar_datos():
    try:
        with open(archivos_datos_alumnos, 'r') as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        return {}


def guardar_datos():
    with open(archivos_datos_alumnos, 'w') as archivo:
        json.dump(alumnos, archivo, indent=4)

alumnos = cargar_datos()

def buscar():
    print("Ingrese un DNI para verificar")
    while True:
        try:
            dni =input("Por favor ingrese un DNI: ")
            dni_int=int(dni)   
            if dni_int > 0: 
                if dni in alumnos:
                    mostrar_alumno(dni)
                    break
                else:
                    print("DNI no encontrado. ¿Desea agregarlo?")
                    rta = input("Ingrese (S) para agregar o (N) para salir: ")
                    if rta.upper() == "S":
                        obtener_datos(dni)
                        break
                    elif rta.upper() == "N":
                        print("Operación cancelada.")
                        buscar()
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")
            else:
                raise ValueError("Debe ingresar un número positivo de DNI válido.")
        except ValueError as error:
            print("Debe ingresar un número de DNI válido.")
            print("Codigo de error :",error)
    
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
            try:
                nuevo_nombre = input("Ingrese nuevo nombre: ")
                if nuevo_nombre.strip() == "":  
                    break
                if nuevo_nombre.isalpha(): 
                    alumno["Nombre"] = nuevo_nombre.upper()
                    print("Nuevo nombre es", alumno["Nombre"])
                    print("")
                    guardar_datos()  
                    mostrar_alumno(dni)
                    break
                else:
                    raise ValueError("Por favor ingrese un nombre válido.")
            except ValueError as error:
                print(error)
        if not nuevo_nombre.strip():
            print("Se mantiene el mismo")
            mostrar_alumno(dni)

    elif editor.upper() == "APELLIDO":
        while True:
            try:
                nuevo_apellido=input("Ingrese nuevo Apellido")
                if nuevo_apellido.strip()=="":
                    break
                if nuevo_apellido.isalpha:
                    alumno["Apellido"]= nuevo_apellido.upper()
                    print("El nuevo apelido es ",alumno["Apellido"])  
                    print("")  
                    guardar_datos()  
                    mostrar_alumno(dni)
                    break
                else:
                    raise ValueError("Por favor ingrese un Apellido valido")
            except ValueError as error:
                print(error)    
                 
        if not nuevo_apellido.strip():
            print("No se ha ingresado un Apellido se mantiene el mismo")
            print("")
            mostrar_alumno(dni)
                  
    elif editor.upper() == "FECHA DE NACIMIENTO":
        #Dia 
        while True:
            try:
                dia = input("Ingrese DIA de nacimiento: ")
                if dia.strip()=="":
                    break
                if dia.isnumeric():
                    dia = int(dia)
                    if dia > 0 and dia <= 31:
                        print("Día válido:", dia)
                        break
                    else:
                        raise ValueError("El día debe estar entre 1 y 31. ")
                else:
                    raise ValueError("Ingrese un número entero para el día.")
            except ValueError as error:
                print(error)
        if not dia.strip():
            print("Se mantiene el mismo")
        while True:
            try:
                mes = input("Ingrese MES de nacimiento: ")
                if mes.strip()=="":
                    break
                if mes.isnumeric():
                    mes = int(mes)
                    if mes >0 and mes <=12:
                        print("Mes válido:", mes)
                        break
                    else:
                        raise ValueError("El MES debe estar entre 1 y 12. ")
                else:
                    raise ValueError("Ingrese un número entero para el mes.")
            except ValueError as error:
                print(error)
        if not mes.strip():
            print("Se mantiene el mismo")
        
        while True:
            try:
                año = input("Ingrese AÑO de nacimiento: ")
                if año.strip()=="":
                    break
                if año.isnumeric():
                    año = int(año)
                    if año > 1980 and año <= 2020:#En este caso puse un rango asi porque los alumnos pueden variar, pero como para no exagerar les deje esos limite
                        print("Año válido:", año)
                        break
                    else:
                        raise ValueError("El Año debe estar entre 1970 y 2020. ")
                else:
                    raise ValueError("Ingrese un número entero para el Año.")
            except ValueError as error:
                print(error)    
        if not año.strip():
            print("Se mantiene el mismo")     
                 
        new_fecha_nac=dia,mes,año
        if new_fecha_nac:
            alumno["Fecha de nacimiento"]= new_fecha_nac
            print("Nueva fecha de nacimiento ",alumno["Fecha de nacimiento"])
            print("")
            guardar_datos()  
            modificar_alumnos(dni)
    
               
    elif editor.upper() == "DNI":
        while True:
            try:
                
                new_dni=input("Ingrese DNI")
                if new_dni.strip()=="":
                    break
                if new_dni.isnumeric():
                    alumno["DNI"]=new_dni
                    print("Dni valido es ",alumno["DNI"])
                    guardar_datos() 
                    mostrar_alumno(dni)
                    break
                else:
                    raise ValueError("Ingrese un dato valido")    
            except ValueError as error:
                print(error)            
        if not new_dni.strip():
            print("Se mantiene")  
            mostrar_alumno(dni)    
             
    elif editor.upper() == "TUTOR":
        #NOMBRE DE TUTOR
        while True:
            try:
                new_nombre_tutor = input("Ingrese nuevo nombre :  ")
                if new_nombre_tutor.strip() == "":  
                    break
                if new_nombre_tutor.isalpha(): 
                    new_nombre_tutor=new_nombre_tutor
                    print("Nuevo nombre Tutor es", new_nombre_tutor)
                    print("")
                    break
                else:
                    raise ValueError("Por favor ingrese un nombre válido.")
            except ValueError as error:
                print(error)
        if not new_nombre_tutor.strip():
            print("Se mantiene el mismo")
            mostrar_alumno(dni)
            
            
        #APELLIDO DE TUTOR   
        while True:
            try:
                new_apellido_tutor = input("Ingrese nuevo Apellido :  ")
                if new_apellido_tutor.strip() == "":  
                    break
                if new_apellidotutor.isalpha:
                    new_apellidotutor=new_apellido_tutor
                    print("Nuevo Apellido Tutor es", new_apellido_tutor)
                    print("")
                    break
                else:
                    raise ValueError("Por favor ingrese un Apellido válido.")
            except ValueError as error:
                print(error)
        if not new_apellido_tutor.strip():
            print("Se mantiene el mismo")
            mostrar_alumno(dni)
            
        tutor=new_nombre_tutor,new_apellido_tutor
        alumno["Tutor"]=tutor
        print("Nuevo Nombre de Tutor es", alumno["Tutor"])
        guardar_datos() 
                      
    elif editor.upper() == "NOTAS": 
        while True:
            try:
                new_nota=input("Ingrese Nota")
                if new_nota.strip()=="":
                    break
                if new_nota.isnumeric():
                    alumno["Nota"]+=new_nota
                    print("Nota valida : ",alumno["Nota"])
                    guardar_datos() 
                    mostrar_alumno(dni)
                    break
                else:
                    raise ValueError("Ingrese un dato valido")    
            except ValueError as error:
                print(error)            
        if not new_nota.strip():
            print("Se mantiene")  
            mostrar_alumno(dni)   
                 
    elif editor.upper() == "FALTAS": 
        print("Faltas actuales",alumno["Faltas"])
        while True:
            try:
                new_falta=input("Ingrese Falta")
                if new_falta.strip()=="":
                    break
                if new_falta.isnumeric():
                    alumno["Faltas"]=new_falta
                    print("Nueva Falta  : ",alumno["Faltas"])
                    guardar_datos() 
                    mostrar_alumno(dni)
                    break
                else:
                    raise ValueError("Ingrese un dato valido")    
            except ValueError as error:
                print(error)            
        if not new_falta.strip():
            print("Se mantiene")  
            mostrar_alumno(dni)   
            
    elif editor.upper() == "AMONESTACIONES": 
        print("Amonestaciones actuales ",alumno["Amonestaciones"])
        while True:
            try:
                new_amonestaciones=input("Ingrese Falta")
                if new_amonestaciones.strip()=="":
                    break
                if new_amonestaciones.isnumeric():
                    alumno["Faltas"]+=new_amonestaciones
                    print("Nueva amonestacion : ",alumno["Amonestaciones"])
                    guardar_datos()  
                    mostrar_alumno(dni)
                    break
                else:
                    raise ValueError("Ingrese un dato valido")    
            except ValueError as error:
                print(error)            
        if not new_amonestaciones.strip():
            print("Se mantiene")  
            mostrar_alumno(dni)  
                    
    elif editor.upper()=="S":
        print("Atras")
        print("")
        mostrar_alumno(dni)
    else:
        print("Por favor escriba correctamente")
        print("")
        modificar_alumnos(dni)    
               
def obtener_datos(dni):
    #nombre
    while True:
        try:
            nombre = input("Ingrese nuevo nombre: ")
            if nombre.isalpha(): 
                nombre=nombre
                break
            else:
                raise ValueError("Por favor ingrese un nombre válido.")
        except ValueError as error:
                print(error)
   
        
    #apellido
    while True:
        try:
            apellido = input("Ingrese el apellido del alumno: ")
            if apellido.isalpha():
                apellido=apellido
                break
            else:
                raise ValueError("Por favor ingrese un apellido valido")   
        except ValueError as error:
            print(error)              
    #DNI
    while True:
          try:
              dni=input("Ingrese DNI")
              if dni.isnumeric():
                  dni=dni
                  break
              else:
                  raise ValueError("Ingrese un dato valido")    
          except ValueError as error:
              print(error)     
              
    #FECHA DE NACIMIENTO           
    print("Ingrese la fecha de nacimiento del alumno (dd/mm/aaaa): ")
            #Dia 
    while True:
            try:
                dia = input("Ingrese DIA de nacimiento: ")
                if dia.isnumeric():
                    dia = int(dia)
                    if dia > 0 and dia <= 31:
                        print("Día válido:", dia)
                        dia=dia
                        break
                    else:
                        raise ValueError("El día debe estar entre 1 y 31. ")
                else:
                    raise ValueError("Ingrese un número entero para el día.")
            except ValueError as error:
                print(error)
    while True:
            try:
                mes = input("Ingrese MES de nacimiento: ")
                if mes.isnumeric():
                    mes = int(mes)
                    if mes >0 and mes <=12:
                        print("Mes válido:", mes)
                        mes=mes
                        break
                    else:
                        raise ValueError("El MES debe estar entre 1 y 12. ")
                else:
                    raise ValueError("Ingrese un número entero para el mes.")
            except ValueError as error:
                print(error)
        
        
    while True:
            try:
                año = input("Ingrese AÑO de nacimiento: ")
                if año.isnumeric():
                    año = int(año)
                    if año > 1980 and año <= 2020:#En este caso puse un rango asi porque los alumnos pueden variar, pero como para no exagerar les deje esos limite
                        print("Año válido:", año)
                        break
                    else:
                        raise ValueError("El Año debe estar entre 1970 y 2020. ")
                else:
                    raise ValueError("Ingrese un número entero para el Año.")
            except ValueError as error:
                print(error)    
            
    fecha_nacimiento=dia,mes,año
    
    #TUTOR
    #NOMBRE DE TUTOR
    print("Ingrese datos del TUTOR ")
    while True:
            try:
                new_nombre_tutor = input("Ingrese  nombre :  ")
                if new_nombre_tutor.isalpha(): 
                    new_nombre_tutor=new_nombre_tutor
                    print("Nuevo nombre Tutor es", new_nombre_tutor)
                    break
                else:
                    raise ValueError("Por favor ingrese un nombre válido.")
            except ValueError as error:
                print(error)
     
            
            
    #APELLIDO DE TUTOR   
    
    while True:
            try:
                new_apellido_tutor = input("Ingrese  Apellido del tutor :  ")
                if new_apellido_tutor.isalpha(): 
                    new_apellido_tutor=new_apellido_tutor
                    print("Nuevo Apellido Tutor es", new_apellido_tutor)
                    print("")
                    break
                else:
                    raise ValueError("Por favor ingrese un Apellido válido.")
            except ValueError as error:
                print(error)
        
            
    tutor=new_nombre_tutor,new_apellido_tutor 
    nuevo_alumno=carga_datos_alumnos(nombre,apellido,dni,fecha_nacimiento,tutor)
    alumnos[dni]=nuevo_alumno
    guardar_datos()  
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
            guardar_datos()  
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
buscar()
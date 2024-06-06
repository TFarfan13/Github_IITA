import json

ARCHIVO_DATOS_ALUMNOS = "alumnos1.js"

class Alumno:
    def __init__(self, nombre, apellido, dni, fecha_nacimiento, tutor, notas=None, faltas=0, amonestaciones=0):
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.tutor = tutor
        self.notas = notas if notas is not None else []
        self.faltas = faltas
        self.amonestaciones = amonestaciones

    def mostrar(self):
        print(f"Nombre: {self.nombre}\n"
              f"Apellido: {self.apellido}\n"
              f"Fecha de nacimiento: {self.fecha_nacimiento}\n"
              f"DNI: {self.dni}\n"
              f"Tutor: {self.tutor}\n"
              f"Notas: {self.notas}\n"
              f"Faltas: {self.faltas}\n"
              f"Amonestaciones: {self.amonestaciones}")
    
    def modificar(self, campo, valor):
        if hasattr(self, campo):
            setattr(self, campo, valor)
        else:
            print("Campo no válido")

class GestionAlumnos:
    def __init__(self):
        self.alumnos = self.cargar_datos()

    def cargar_datos(self):
        try:
            with open(ARCHIVO_DATOS_ALUMNOS, 'r') as archivo:
                datos = json.load(archivo)
                alumnos = {}
                for dni, info in datos.items():
                    alumnos[dni] = Alumno(
                        nombre=info["Nombre"],
                        apellido=info["Apellido"],
                        dni=info["DNI"],
                        fecha_nacimiento=info["Fecha de nacimiento"],
                        tutor=info["Tutor"],
                        notas=info["Notas"],
                        faltas=info["Faltas"],
                        amonestaciones=info["Amonestaciones"]
                    )
                return alumnos
        except FileNotFoundError:
            return {}

    def guardar_datos(self):
        with open(ARCHIVO_DATOS_ALUMNOS, 'w') as archivo:
            json.dump({dni: alumno.__dict__ for dni, alumno in self.alumnos.items()}, archivo, indent=4)

    def buscar(self, dni):
        if dni in self.alumnos:
            self.alumnos[dni].mostrar()
        else:
            print("DNI no encontrado. ¿Desea agregarlo?")
            rta = input("Ingrese (S) para agregar o (N) para salir: ")
            if rta.upper() == "S":
                self.obtener_datos(dni)

    def obtener_datos(self, dni):
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

        nuevo_alumno = Alumno(nombre, apellido, dni, fecha_nacimiento, tutor)
        self.alumnos[dni] = nuevo_alumno
        self.guardar_datos()

    def modificar_alumno(self, dni):
        if dni in self.alumnos:
            alumno = self.alumnos[dni]
            alumno.mostrar()
            campo = input("Ingrese el campo a modificar (nombre, apellido, fecha_nacimiento, tutor, notas, faltas, amonestaciones): ")
            valor = input(f"Ingrese el nuevo valor para {campo}: ")
            if campo == "notas":
                valor = list(map(int, valor.split(',')))
            elif campo in ["faltas", "amonestaciones"]:
                valor = int(valor)
            alumno.modificar(campo, valor)
            self.guardar_datos()
        else:
            print("Alumno no encontrado.")

    def eliminar_alumno(self, dni):
        if dni in self.alumnos:
            del self.alumnos[dni]
            self.guardar_datos()
            print("Alumno eliminado.")
        else:
            print("Alumno no encontrado.")

def main():
    gestion = GestionAlumnos()
    while True:
        accion = input("¿Qué desea accion desea realizar? (buscar, modificar, eliminar, salir): ")
        if accion.lower() == "salir":
            break
        dni = input("Ingrese el DNI del alumno: ")
        if accion.lower() == "buscar":
            gestion.buscar(dni)
        elif accion.lower() == "modificar":
            gestion.modificar_alumno(dni)
        elif accion.lower() == "eliminar":
            gestion.eliminar_alumno(dni)
        else:
            print("Acción no válida.")

if __name__ == "__main__":
    main()

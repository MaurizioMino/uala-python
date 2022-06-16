class Alumno:

    cantidad_alumnos = 0
    registro_alumnos = []

    def __init__(self, legajo, nombre, apellido, notas):
        self.legajo = legajo
        self.nombre = nombre
        self.apellido = apellido
        Alumno.cantidad_alumnos += 1
        self.notas = notas
        Alumno.registro_alumnos.append(self)
        self.promedio = self.dar_promedio()
    

    def cargar_nota(self, nota):
        self.notas.append(nota)
        self.promedio = self.dar_promedio()


    def dar_alumno(self):
        return (f'Legajo {self.legajo} | Apellido {self.apellido} | Nombre {self.nombre} | Promedio {self.promedio}')


    def dar_nota(self):
        for nota in self.notas:
            print(nota)

    
    def dar_alumnos():
        registro = []
        for alumno in Alumno.registro_alumnos:
            datos_alumnos = {"legajo" : alumno.legajo, "apellido": alumno.apellido, "nombre": alumno.nombre}
            registro.append(datos_alumnos)
        return registro

    
    def dar_promedio(self):
        return sum(self.notas) / len(self.notas)


    def mayor_nota(self):
        return max(self.notas)
    



# Programa principal
a = Alumno(123, "Azul", "Quiroga", [1, 2, 3])
b = Alumno(123, "Juan", "Lopez", [1, 2, 3])
c = Alumno(123, "Sebastian", "Korach", [1, 2, 3])
d = Alumno(123, "Azul", "Celeste", [1, 2, 3])
e = Alumno(123, "Azul", "Rosa", [1, 2, 3])


print(f'Primer alumno\n')
print(a.dar_alumno())
print("")

print(f'Mostrar notas\n')
a.dar_nota()
print("")

print(f'Cargar nota 7\n')
a.cargar_nota(7)
print("")

print(f'Mostrar notas\n')
a.dar_nota()
print("")

print(f'Promedio de notas de {a.dar_alumno()} \n')
print(a.dar_promedio())
print("")
print(f'Nota más alta:\n')
print(a.mayor_nota())
print("")


print(Alumno.dar_alumnos())
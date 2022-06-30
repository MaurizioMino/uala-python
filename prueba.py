class Alumnos:

    alumnos = []


    def __init__(self, nombre, apellido, edad, notas):
        self.name = nombre
        self.apellido = apellido
        self.edad = edad
        self.notas = notas
        Alumnos.alumnos.append(self)
        self.promedio = self.promedio()


    def promedio(self):
        return sum(self.notas) / len(self.notas)

    def dar_info_alumno( self ):
        return f'Name: {self.name}\nApellido: {self.apellido}\nEdad: {self.edad}\nNotas: {self.notas}\n'


    @staticmethod
    def contar_alumnos( ):
        return len(Alumnos.alumnos)


a = Alumnos("Maria", "Perez", 20, [6, 1, 3, 3, 4])

print(a.dar_info_alumno)
print(a.promedio)
print(Alumnos.promedio)
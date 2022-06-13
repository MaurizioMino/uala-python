class Alumnos:

    alumnos = []
    #notas = []


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
b = Alumnos("Juan", "Ramirez", 18, [10, 10, 10, 10, 10])
c = Alumnos("Pablo", "Ramirez", 19, [6, 0, 2, 3, 9])
d = Alumnos("Carmen", "Velazquez", 20, [10, 10, 2, 3, 9])

lista_alumnos = [(a.name + a.apellido), (b.name+ b.apellido), (c.name+c.apellido), (d.name+ d.apellido)]

print ("los alumnos creados son:" + str(lista_alumnos))

print ("Informacion del alumno:")
print (b.dar_info_alumno())

print("la cantidad de alumnos son:")
print(Alumnos.contar_alumnos())

print("El promedio del alumno a es:", a.promedio)
print("El promedio del alumno b es:", b.promedio)
print("El promedio del alumno c es:", c.promedio)
print("El promedio del alumno d es:", d.promedio)


max_value = None

for num in a.notas:
    if (max_value is None or num > max_value):
       max_value = num

print('la nota mas alta del alumno a es:', max_value)

lista_de_promedios = [3.4, 10.0, 4.0, 6.8]
max_promedio = None
for num in lista_de_promedios:
      if (max_promedio is None or num > max_promedio):
       max_promedio = num

print ("El promedio mas alto es:", max_promedio)


min_promedio = None

for num in lista_de_promedios:
    if (min_promedio is None or num < min_promedio):
       min_promedio = num

print ("El promedio mas bajo es:", min_promedio )

#Generar método que elija al estudiante con mejor nota




















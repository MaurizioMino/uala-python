notas = [1, 10, 9, 2, 3, 4, 5, 6, 7, 8]
cantidad_notas = 10

suma_de_notas = 0

# Metodos para el promedio suma
# metodo1
for nota in notas:
    suma_de_notas += nota
print("La sumatoria de las notas es:")
print(suma_de_notas)

promedio = suma_de_notas / float(cantidad_notas)
print("El promedio calculado es:")
print(promedio)

# metodo2 funcion sum

suma_de_notas = sum(notas)
print("La sumatoria de las notas usando la funcion sum es:")
print(suma_de_notas)

promedio = sum(notas) / float(len(notas))
print("El promedio de nota es:")
print(promedio)

# Iterar a traves de un diccionario con un for para imprimir un texto con ambos valores (Minimo 5 elementos)

diccionario = {"raza": "caniche", "color": "blanco", "edad": 2, "animal": "perro", "nombre": "teddy"}
keys = diccionario.keys()

for key in diccionario:
    print(key, ":", diccionario[key])

# Realizar un while que agregue un carácter o un elemento a alguna variable hasta que supere un largo de 8 elementos(empezar de algo vacío). Imprimir cada iteración

reloj = 0
hora = ['las trece', 'las catorce', 'las quince', 'las dieciseis', 'las diecisiete', 'las dieciocho', 'las diecinueve',
        'las veinte']
while reloj < 8:
    print("la hora es: " + hora[reloj])
    reloj += 1



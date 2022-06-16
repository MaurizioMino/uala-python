a = 1
b = 2
c = 3

print("primer numero aparece la misma cantidad de veces que el segundo:")
print(str(a) * b)
print("segundo numero es:")
print(b)

# sumatoria de los 3 numeros
print("la sumatoria de los numeros es:")
print(a + b + c)

# promedio
print("el promedio de los numeros es:")
print(int(a + b + c) / 3)

# 3.Pedir 4 palabras y unirlas con guiones bajos

lista_1 = ['mi', 'nombre', 'es:', 'Emileth']
sep = '_'
nueva_string = sep.join(lista_1)
print(nueva_string)

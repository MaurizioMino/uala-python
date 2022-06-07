# 1. Crear un método para el promedio y la suma

def suma (a, b):
    return a +  b

def promedio(lista):
    return sum(lista) / len(lista)

lista_a = [1, 2, 3, 4]


print(suma(1, 2))
print(promedio(lista_a))


# 2. Iterar a través de un array y que muestre el promedio de los datos(minimo 10 elementos)

for elemento in lista_a:
    print(elemento)


# 3. Iterar a traves de un diccionario con un for para imprimir un texto con ambos valores (Minimo 5 elementos)

diccionario_A = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}




# 4. Realizar un while que agregue un caracter o un element a alguna variable, hasta que supere un largo de 8 
# elementos (empezar de algo vacio). Imprimir cada iteracion.
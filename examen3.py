# ------------------------------------------------------------
# 1. CREAR E INICIALIZAR LISTAS
# ------------------------------------------------------------
# Una lista permite almacenar varios elementos en una sola
# variable. Se define utilizando corchetes [] y sus elementos
# se separan mediante comas.
# Ejemplo:

numeros = [10, 20, 30, 40, 50]
otros_numeros = [5, 15, 25, 35, 45]

print("1. CREAR E INICIALIZAR LISTAS")
print("Lista principal:", numeros)
print("Segunda lista:", otros_numeros)


# ------------------------------------------------------------
# 2. SUMAR Y CONTAR ELEMENTOS
# ------------------------------------------------------------
# sum(): calcula la suma de los elementos numéricos.
# len(): devuelve la cantidad de elementos de la lista.
# min(): obtiene el valor mínimo.
# max(): obtiene el valor máximo.

print("\n2. SUMAR Y CONTAR ELEMENTOS")

print("Suma de los números:", sum(numeros))
print("Cantidad de elementos:", len(numeros))
print("Número menor:", min(numeros))
print("Número mayor:", max(numeros))


# ------------------------------------------------------------
# 3. BUSCAR Y CONTAR ELEMENTOS
# ------------------------------------------------------------
# in: verifica si un elemento se encuentra en la lista.
# index(): devuelve la posición de la primera coincidencia.
# count(): cuenta cuántas veces aparece un elemento.

print("\n3. BUSCAR Y CONTAR ELEMENTOS")

print("¿Existe el número 30?", 30 in numeros)
print("Posición del número 40:", numeros.index(40))

numeros_repetidos = [10, 20, 10, 30, 10, 40]

print("Cantidad de veces que aparece 10:",
      numeros_repetidos.count(10))


# ------------------------------------------------------------
# 4. COMPARAR Y COMBINAR LISTAS
# ------------------------------------------------------------
# El operador + une dos listas y genera una nueva.
# El operador == permite comprobar si dos listas son iguales.
# El operador * repite los elementos de una lista.

print("\n4. COMPARAR Y COMBINAR LISTAS")

lista_combinada = numeros + otros_numeros

print("Listas combinadas:", lista_combinada)
print("¿Son iguales ambas listas?", numeros == otros_numeros)

lista_repetida = [1, 2, 3] * 3

print("Lista repetida:", lista_repetida)


# ------------------------------------------------------------
# 5. COPIAR Y ELIMINAR ELEMENTOS
# ------------------------------------------------------------
# copy(): crea una copia independiente de la lista.
# clear(): elimina todos los elementos de una lista.
# pop(): elimina y devuelve un elemento por su índice.
# remove(): elimina la primera coincidencia de un valor.

print("\n5. COPIAR Y ELIMINAR ELEMENTOS")

copia_numeros = numeros.copy()

print("Copia de la lista:", copia_numeros)

elemento_eliminado = copia_numeros.pop()

print("Elemento eliminado:", elemento_eliminado)
print("Lista después de pop():", copia_numeros)

copia_numeros.remove(20)

print("Lista después de remove():", copia_numeros)

copia_numeros.clear()

print("Lista después de clear():", copia_numeros)


# ------------------------------------------------------------
# 6. ORDENAR Y REALIZAR OPERACIONES CONJUNTAS
# ------------------------------------------------------------
# sort(): ordena los elementos de la lista original.
# reverse(): invierte el orden actual de los elementos.
# sorted(): devuelve una nueva lista ordenada.
# Las listas numéricas también pueden utilizarse para
# realizar cálculos estadísticos sencillos.

print("\n6. ORDENAR Y REALIZAR OPERACIONES CONJUNTAS")

numeros.sort()

print("Lista ordenada:", numeros)

numeros.reverse()

print("Lista en orden inverso:", numeros)

promedio = sum(numeros) / len(numeros)

print("Promedio de los números:", promedio)

# FIN DEL PROGRAMA
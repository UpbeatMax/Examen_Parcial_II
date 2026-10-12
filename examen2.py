# ------------------------------------------------------------
# 1. ¿QUÉ SON LAS COLECCIONES ORDENADAS?
# ------------------------------------------------------------
# Una tupla es una colección ordenada que permite almacenar
# varios elementos en una sola variable.
# Sus elementos conservan su posición y pueden consultarse
# mediante índices que comienzan desde 0.
# A diferencia de las listas, las tuplas son inmutables,
# es decir, no pueden modificarse directamente.
#
# Ejemplo:

colores = ("Azul", "Rojo", "Verde", "Amarillo")

print("1. COLECCIONES ORDENADAS")
print("Tupla de colores:", colores)


# ------------------------------------------------------------
# 2. ACCEDER Y MODIFICAR ELEMENTOS
# ------------------------------------------------------------
# Se utilizan índices positivos o negativos para acceder
# a los elementos de una tupla.
# Como las tuplas son inmutables, para modificar un elemento
# se convierte la tupla en lista y después nuevamente en tupla.

print("\n2. ACCEDER Y MODIFICAR")

print("Primer color:", colores[0])
print("Último color:", colores[-1])

colores_lista = list(colores)
colores_lista[1] = "Morado"
colores = tuple(colores_lista)

print("Tupla modificada:", colores)


# ------------------------------------------------------------
# 3. AGREGAR Y ELIMINAR ELEMENTOS
# ------------------------------------------------------------
# Las tuplas no permiten agregar ni eliminar elementos
# directamente.
# Para realizar estas operaciones, se convierten en listas
# y posteriormente se vuelven a convertir en tuplas.

print("\n3. AGREGAR Y ELIMINAR")

colores_lista = list(colores)

# Agregar un elemento al final.
colores_lista.append("Naranja")

# Eliminar un elemento por su valor.
colores_lista.remove("Verde")

colores = tuple(colores_lista)

print("Tupla después de agregar y eliminar:", colores)


# ------------------------------------------------------------
# 4. MEDIR Y CORTAR TUPLAS
# ------------------------------------------------------------
# len(): devuelve la cantidad de elementos.
# El slicing permite obtener una sección de la tupla.
# La posición final indicada no se incluye en el resultado.

print("\n4. MEDIR Y CORTAR")

print("Cantidad de colores:", len(colores))
print("Primeros dos colores:", colores[0:2])
print("Colores desde la segunda posición:", colores[1:])
print("Últimos dos colores:", colores[-2:])


# ------------------------------------------------------------
# 5. ORDENAR Y VERIFICAR ELEMENTOS
# ------------------------------------------------------------
# sorted(): devuelve una lista con los elementos ordenados.
# Para obtener nuevamente una tupla, se utiliza tuple().
# El operador in permite verificar si un elemento existe.
# Los elementos deben ser comparables para poder ordenarse.

print("\n5. ORDENAR Y VERIFICAR")

colores_ordenados = tuple(sorted(colores))

print("Tupla ordenada:", colores_ordenados)

print("¿Existe el color Azul?", "Azul" in colores)
print("¿Existe el color Negro?", "Negro" in colores)


# ------------------------------------------------------------
# 6. UNIR TUPLAS
# ------------------------------------------------------------
# El operador + permite concatenar dos o más tuplas.
# El resultado es una nueva tupla que contiene los elementos
# de ambas colecciones en el orden en que fueron combinadas.

print("\n6. UNIR TUPLAS")

colores_calidos = ("Rojo", "Naranja", "Amarillo")
colores_frios = ("Azul", "Verde", "Morado")

colores_combinados = colores_calidos + colores_frios

print("Tuplas combinadas:", colores_combinados)

# FIN DEL PROGRAMA

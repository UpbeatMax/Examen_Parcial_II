# 1. ¿QUÉ SON LAS LISTAS EN PYTHON?
# ------------------------------------------------------------
# Una lista es una estructura de datos que permite almacenar
# varios elementos en una sola variable. Sus elementos pueden
# ser de diferentes tipos y se identifican mediante índices,
# comenzando desde la posición 0.
#
# Ejemplo:

frutas = ["Manzana", "Pera", "Naranja", "Plátano"]

print("1. LISTAS EN PYTHON")
print("Lista de frutas:", frutas)


# ------------------------------------------------------------
# 2. ACCEDER Y MODIFICAR ELEMENTOS
# ------------------------------------------------------------
# Para acceder a un elemento se utiliza su índice.
# Para modificarlo, se asigna un nuevo valor a esa posición.

print("\n2. ACCEDER Y MODIFICAR")

print("Primera fruta:", frutas[0])
print("Última fruta:", frutas[-1])

frutas[1] = "Uva"

print("Lista modificada:", frutas)


# ------------------------------------------------------------
# 3. AGREGAR Y ELIMINAR ELEMENTOS
# ------------------------------------------------------------
# append(): agrega un elemento al final.
# insert(): agrega un elemento en una posición específica.
# remove(): elimina la primera coincidencia de un valor.
# pop(): elimina un elemento mediante su índice.
# del: elimina un elemento o una sección de la lista.

print("\n3. AGREGAR Y ELIMINAR")

frutas.append("Mango")
frutas.insert(1, "Fresa")

print("Después de agregar:", frutas)

frutas.remove("Naranja")
frutas.pop(0)

print("Después de eliminar:", frutas)


# ------------------------------------------------------------
# 4. MEDIR Y CORTAR LISTAS
# ------------------------------------------------------------
# len(): devuelve la cantidad de elementos de una lista.
# El slicing permite obtener una sección de la lista usando
# la sintaxis lista[inicio:fin], sin incluir el índice final.

print("\n4. MEDIR Y CORTAR")

print("Cantidad de frutas:", len(frutas))
print("Primeros dos elementos:", frutas[0:2])
print("Elementos desde la segunda posición:", frutas[1:])
print("Últimos dos elementos:", frutas[-2:])


# ------------------------------------------------------------
# 5. ORDENAR Y VERIFICAR ELEMENTOS
# ------------------------------------------------------------
# sort(): ordena los elementos de la lista original.
# sorted(): devuelve una nueva lista ordenada.
# reverse=True permite ordenar de mayor a menor o en
# orden alfabético inverso, según el tipo de elementos.
# in: verifica si un elemento existe dentro de la lista.

print("\n5. ORDENAR Y VERIFICAR")

frutas.sort()

print("Lista ordenada:", frutas)

print("¿Existe la manzana?", "Manzana" in frutas)
print("¿Existe la sandía?", "Sandía" in frutas)

frutas.sort(reverse=True)

print("Orden inverso:", frutas)


# ------------------------------------------------------------
# 6. UNIR LISTAS
# ------------------------------------------------------------
# El operador + permite unir dos listas y crear una nueva.
# El método extend() agrega los elementos de otra lista
# al final de la lista original.

print("\n6. UNIR LISTAS")

verduras = ["Zanahoria", "Lechuga", "Pepino"]
otros_alimentos = ["Tomate", "Cebolla"]

lista_unida = verduras + otros_alimentos

print("Listas unidas con +:", lista_unida)

verduras.extend(otros_alimentos)

print("Lista original ampliada con extend():", verduras)

# FIN DEL PROGRAMA
# #LISTAS
# # Se crea una lista de compras con dos elementos: "pan" y "leche"
# compras=["pan","leche"]
# #Se utiliza el método append() para agregar un nuevo elemento 
# #"huevos" al final de la lista de compras
# compras.append("huevos")
# #Se imprime la lista de compras en la consola, mostrando los tres
# #  elementos: "pan", "leche" y "huevos"
# print(compras)

#TUPLA
# # Se crea una tupla llamada "ubicacion" con dos elementos:
# # "casa" y "trabajo"
# ubicacion=("casa","trabajo")
# # Se utiliza el operador += para agregar un nuevo elemento
# # "escuela" a la tupla "ubicacion". Como las tuplas son inmutables, se
# #  crea una nueva tupla que contiene los elementos originales más 
# # el nuevo elemento, y se asigna a la variable "ubicacion"
# ubicacion+=("escuela",)
# # Se imprime la tupla "ubicacion" en la consola, mostrando los tres
# # elementos: "casa", "trabajo" y "escuela"
# print(ubicacion)


# #CONJUNTO
# # Se crea un conjunto llamado "categorias" con dos elementos:
# # "comida" y "bebida"
# categorias={"comida","bebida"}
# # Se utiliza el método add() para agregar un nuevo elemento
# # "Limpieza" al conjunto "categorias". 
# # Como los conjuntos no permiten elementos duplicados, si el elemento
# # ya existe en el conjunto,no se agregará nuevamente. En este caso, "Limpieza" es un nuevo
# categorias.add("Limpieza")
# #Se imprime el conjunto "categorias" en la consola, mostrando los tres
# print(categorias)

#DICCIONARIO
#se crea un diccionario llamado "precios" con un elemento: la clave "pan"
precios={"pan":25}
#Se utiliza la sintaxis de corchetes para agregar un
#  nuevo elemento al diccionario "precios", 
# con la clave "leche" y el valor 30.
precios["leche"]=30
#Se imprime el diccionario "precios" en la consola, mostrando los dos
# elementos: "pan" con valor 25 y "leche" con valor 30
print(precios)
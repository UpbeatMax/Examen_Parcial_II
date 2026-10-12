# PRACTICA : CALCULADORA SIMPLE

# • Pedir a tu ex, nombre, 3 calificaciones y guardarlas en la colección que tu veas necesaria
# • Convertirlas a float cada una
# • Calcular el promedio
# • Mostrar: nombre, calificaciones y promedio
# • Indicar si aprobó (≥ 6.0) o reprobó


#Esta línea solicita al usuario que ingrese su nombre y lo almacena en la variable "nombre"     
nombre = input("Ingrese su nombre: ")
#Estas líneas solicitan al usuario que ingrese tres calificaciones, las convierten a tipo float y las almacenan en variables separadas
calificacion1 = float(input("Ingrese la primera calificación: "))   
calificacion2 = float(input("Ingrese la segunda calificación: "))   
calificacion3 = float(input("Ingrese la tercera calificación: "))   

#Estas líneas crean una lista llamada "calificaciones" que contiene
#las tres calificaciones ingresadas por el usuario, y luego calculan 
# el promedio de esas calificaciones dividiendo la suma de las 
# calificaciones entre la cantidad de calificaciones
calificaciones = [calificacion1, calificacion2, calificacion3]
#El promedio se calcula sumando todas las calificaciones y dividiendo entre el número de calificaciones
promedio = sum(calificaciones) / len(calificaciones)

#En estas lineas se imprimen en pantalla el nombre del usuario, las calificaciones 
# ingresadas y el promedio calculado.
print(f"Nombre: {nombre}")
print(f"Calificaciones: {calificaciones}")
print(f"Promedio: {promedio}")

#En el if se evalúa si el promedio es mayor o igual a 6.0, 
# en cuyo caso se imprime un mensaje indicando que el usuario está aprobado.
if promedio >= 6.0:
    print("Usted esta Aprobado")
else:
    print("Usted esta Reprobado")
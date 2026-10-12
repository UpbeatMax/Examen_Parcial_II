#1-Pasamos de texto a numero
num_str = "42"
num_str = int(num_str)
num_flt = float(num_str)
#2-Ahora pasamos de numero a texto 
edad = 25 
texto = str(edad)
#3-Vamos a definir el numero PI con decimales 
pi = 3.14159
#La funcion round redonde el numero de decimales 
print(round(pi, 2))




# #1-Pedimos el nombre 
# nombre = input("Tu nombre?")
# #2-Pedimos la edad y se convierte en entero con int 
# edad = int(input("Cual es tu edad?"))
# #3-Imprimimos el saludo 
# print("Hola!,", nombre)
# #4-Hacemos la operacion matematica 
# print(f"En 5 años tendras {edad + 5}")








# #1-Declaramos la vareable

# #Se guarda el numero 18 (numero entero int)
# edad = 18
# #Guarda true
# tiene_credencial = True
# #Guarda False
# es_alumno = False

# #2-Las condiciones se evaluan 
# if edad >= 18 and tiene_credencial:
#     print("Cumple las dos condiciones")

#     if edad >= 18 or es_alumno:
#         print("Cumple una condicion")

#         #3- Operador NOT (negacion)
#         if not es_alumno:
#             print("No es alumno")
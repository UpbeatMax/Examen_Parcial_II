texto = "Este es un texto"
print("Texto original:", texto)
print("Índice 0 (texto[0]):", texto[0])
print("Índice 4 (espacio) (texto[4]):", repr(texto[4]))

print("-" * 40)

print("Slicing [0:4]:", texto[0:4])
print("Slicing [:7] (omitir inicio):", texto[:7])
print("Slicing [5:] (omitir fin):", texto[5:])
print("Slicing con negativos [5:-2]:", texto[5:-2])

print("-" * 40)

curso = "Este curso es de JavaScript"
print("Curso original:", curso)
curso_modificado = curso.replace("JavaScript", "Python")
print("Usando replace():", curso_modificado)

print("-" * 40)

texto_dividido = texto.split(" ")
print("Usando split(' '):", texto_dividido)

print("-" * 40)

texto2 = "Este Texto tiene MAYÚSCULAS y minúsculas"
buscado = "mayúsculas"

print("Búsqueda directa (buscado in texto2):", buscado in texto2)
print("Búsqueda normalizada (.lower()):", buscado.lower() in texto2.lower())
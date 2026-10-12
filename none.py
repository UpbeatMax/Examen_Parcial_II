x = None
print("Valor de x:", x)
print("Tipo de x:", type(x))

print("-" * 30)

print("String vacío ('', str):", type(""))     
print("Cero (0, int):", type(0))
print("Falso (False, bool):", type(False))
print("Lista vacía ([], list):", type([]))
print("Ausencia de valor (None):", type(None))

print("-" * 30)

def saludar():
    print("¡Hola desde la función!")
    
resultado = saludar()
print("Resultado de la función:", resultado)
print("Tipo del resultado:", type(resultado)) <class 'NoneType'>[cite: 3]

print("-" * 30)

variable_prueba = None

if variable_prueba is None:
    print("Validación exitosa: La variable no tiene valor (es None).")[cite: 3]
else:
    print("La variable tiene un valor asignado.")
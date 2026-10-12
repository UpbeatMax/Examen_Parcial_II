import random

x = 1
y = 2.5
z = 5 + 1j

print("--- 1 Y 2. TIPOS NUMÉRICOS ---")
print(f"Valor: {x} | Tipo: {type(x)}")
print(f"Valor: {y} | Tipo: {type(y)}")
print(f"Valor: {z} | Tipo: {type(z)}")

print("-" * 40)

print("--- 3. NÚMEROS COMPLEJOS ---")
print("Parte real:", z.real)
print("Parte imaginaria:", z.imag)

print("-" * 40)

print("--- 4. CASTEO BÁSICO ---")
entero_a_flotante = float(1)
flotante_a_entero = int(2.5)

print("float(1) ->", entero_a_flotante)
print("int(2.5) ->", flotante_a_entero)

print("-" * 40)
print("--- 5. CONVERSIÓN A COMPLEX ---")
print("complex(5) ->", complex(5))
print("complex(5.5) ->", complex(5.5))

print("-" * 40)

print("--- 6. NÚMEROS ALEATORIOS ---")
numero_aleatorio = random.randrange(1, 10)
print("Número aleatorio generado (del 1 al 9):", numero_aleatorio)
x = 5
y = 10

print("--- 1. VARIABLES BASE ---")
print("x =", x)
print("y =", y)
print("-" * 30)

print("--- 2 Y 3. OPERACIONES BÁSICAS ---")
print(f"Suma (x + y) -> {x + y}")
print(f"Resta (x - y) -> {x - y}")
print(f"Multiplicación (x * y) -> {x * y}")
print(f"División (y / x) -> {y / x}")
print("-" * 30)

print("--- 4. MÓDULO, POTENCIA Y DIVISIÓN ENTERA ---")
print(f"Módulo (12 % 5) -> {12 % 5}")
print(f"Potencia (y ** x) -> {y ** x}")
print(f"División entera (12 // 5) -> {12 // 5}")
print("-" * 30)

print("--- 5. DETECTAR NÚMEROS PARES ---")
par = 8
impar = 7
print(f"¿El número {par} es par? -> {par % 2 == 0}")
print(f"¿El número {impar} es par? -> {impar % 2 == 0}")
print("-" * 30)

print("--- 6. ORDEN DE PRECEDENCIA ---")
resultado_sin_parentesis = 10 + 5 * 2
print("Sin paréntesis (10 + 5 * 2) =", resultado_sin_parentesis)

resultado_con_parentesis = (10 + 5) * 2
print("Con paréntesis ((10 + 5) * 2) =", resultado_con_parentesis)
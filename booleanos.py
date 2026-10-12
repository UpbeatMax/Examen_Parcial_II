b = True
f = False
print("Tipo de b:", type(b))

print("-" * 30)

print("¿5 > 3? ->", 5 > 3)
print("¿3 > 5? ->", 3 > 5)

print("-" * 30)

print("bool('Hola') ->", bool("Hola"))
print("bool(123) ->", bool(123))
print("bool([1, 2]) ->", bool([1, 2]))

print("-" * 30)

print("Evaluando valores vacíos o falsos:")
print("bool('') ->", bool(""))
print("bool(0) ->", bool(0))
print("bool([]) ->", bool([]))
print("bool(None) ->", bool(None))
print("-" * 30)

print("isinstance(5, int) ->", isinstance(numero, int))

numero_decimal = 5.5
print("isinstance(5.5, int) ->", isinstance(numero_decimal, int))
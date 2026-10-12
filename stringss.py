texto = "Fundamentos de Python"
print("Texto base:", texto)

print("-" * 40)

simples = 'hola'
dobles = "I'm Sergi"
triples = """varias
líneas"""
print("Comillas simples:", simples)
print("Comillas dobles:", dobles)
print("Comillas triples:\n", triples)

print("-" * 40)

palabra = 'murciélago'
print(f"Palabra: '{palabra}'")
print("Longitud con len():", len(palabra))

print("-" * 40)

print('"Python" in texto ->', "Python" in texto)    
print('"python" in texto ->', "python" in texto)       
print('"JavaScript" not in texto ->', "JavaScript" not in texto)

print("-" * 40)

print("A mayúsculas (.upper()):", texto.upper())
print("A minúsculas (.lower()):", texto.lower())

print("-" * 40)

espacios = '   este es el texto   '
print("Original con espacios:", repr(espacios))
print("Limpiando con strip():", repr(espacios.strip()))
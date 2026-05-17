# DEFINICIÓN DE CONJUNTOS
A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}

print("\n********** ANALISIS DE CONJUNTOS **********")

# Intersección
interseccion = A & B

print("\nUsuarios que usan ambas plataformas:")
print("A ∩ B =", interseccion)

# Unión
union = A | B

print("\nUsuarios registrados en al menos una plataforma:")
print("A ∪ B =", union)

# Usuarios sin errores
sin_errores = union - C

print("\nUsuarios sin errores:")
print("(A ∪ B) - C =", sin_errores)

# Usuarios sospechosos
sospechosos = C - union

print("\nUsuarios sospechosos:")
print("C - (A ∪ B) =", sospechosos)
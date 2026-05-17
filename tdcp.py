# DEFINICIÓN DE CONJUNTOS
A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}

print("\n********** ANALISIS COMPLETO **********")

# Operaciones de conjuntos
print("\nUsuarios en ambas plataformas:")
print(A & B)

print("\nUsuarios registrados en plataformas:")
print(A | B)

print("\nUsuarios sin errores:")
print((A | B) - C)

print("\nUsuarios exclusivos de una plataforma:")
print((A - B) | (B - A))

print("\nUsuarios sospechosos:")
print(C - (A | B))

# FUNCIÓN LÓGICA
def usuario_critico(p, q, r):
    return (p or q) and r

# CLASIFICACIÓN
todos = A | B | C

criticos = []
no_criticos = []

for usuario in todos:

    p = usuario in A
    q = usuario in B
    r = usuario in C

    if usuario_critico(p, q, r):
        criticos.append(usuario)
    else:
        no_criticos.append(usuario)

print("\nUsuarios críticos:")
print(criticos)

print("\nUsuarios no críticos:")
print(no_criticos)

# INTERPRETACIÓN
print("\nINTERPRETACION")

print("\nLos usuarios críticos representan mayor riesgo")
print("porque utilizan plataformas y generan errores.")

print("\nLos usuarios sospechosos generan errores")
print("pero no figuran registrados en API o WEB.")
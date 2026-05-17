# DEFINICIÓN DE CONJUNTOS
A = {101, 102, 103, 104, 105, 106}
B = {104, 105, 106, 107, 108}
C = {102, 105, 109}

print("\n********** LOGICA PROPOSICIONAL **********")

# TABLA DE VERDAD
print("p\tq\tr\t(p∨q)∧r")

valores = [False, True]

for p in valores:
    for q in valores:
        for r in valores:

            resultado = (p or q) and r

            print(f"{p}\t{q}\t{r}\t{resultado}")

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
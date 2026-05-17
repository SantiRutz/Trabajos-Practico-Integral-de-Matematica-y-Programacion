# DEFINICIÓN DE CONJUNTOS
A = {101, 102, 103, 104, 105, 106} # A = usuarios API
B = {104, 105, 106, 107, 108} # B = usuarios WEB
C = {102, 105, 109} # C = usuarios con errores

# PARTE A — ANÁLISIS CON CONJUNTOS
print("\n********** PARTE A - TEORIA DE CONJUNTOS **********")

# 1) Usuarios que utilizan ambas plataformas
ambas_plataformas = A & B

print("\n1) Usuarios que utilizan ambas plataformas:")
print("A ∩ B =", ambas_plataformas)

# 2) Usuarios que utilizan al menos una plataforma
al_menos_una = A | B

print("\n2) Usuarios que utilizan al menos una plataforma:")
print("A ∪ B =", al_menos_una)

# 3) Usuarios que utilizan plataforma pero no presentan errores
sin_errores = (A | B) - C

print("\n3) Usuarios que utilizan plataforma pero no presentan errores:")
print("(A ∪ B) - C =", sin_errores)

# 4) Usuarios que utilizan exclusivamente una sola plataforma
solo_una = (A - B) | (B - A)

print("\n4) Usuarios que utilizan exclusivamente una sola plataforma:")
print("(A - B) ∪ (B - A) =", solo_una)

# 5) Expresión por comprensión de conjuntos
print("\n5) Comprensión de conjuntos:")

comprension_1 = {x for x in A if x in B}
print("Usuarios en ambas plataformas:")
print("{x / x pertenece a A y x pertenece a B}")
print("Resultado:", comprension_1)

comprension_2 = {x for x in (A | B) if x not in C}
print("\nUsuarios sin errores:")
print("{x / x pertenece a (A ∪ B) y x no pertenece a C}")
print("Resultado:", comprension_2)

# 6) Usuarios que aparecen en C pero no en A ∪ B
sospechosos = C - (A | B)

print("\n6) Usuarios que están en C pero no en A ∪ B:")
print("C - (A ∪ B) =", sospechosos)

# PARTE B — LÓGICA PROPOSICIONAL
print("\n********** PARTE B - LOGICA PROPOSICIONAL **********")

# 5) TABLA DE VERDAD
print("\nTABLA DE VERDAD")
print("p\tq\tr\t(p∨q)∧r")

valores = [False, True]

for p in valores:
    for q in valores:
        for r in valores:

            resultado = (p or q) and r

            print(f"{p}\t{q}\t{r}\t{resultado}")

# 6) FUNCIÓN EN PYTHON
def usuario_critico(p, q, r):
    return (p or q) and r

# 7) CLASIFICACIÓN DE USUARIOS
todos_los_usuarios = A | B | C

criticos = []
no_criticos = []

for usuario in todos_los_usuarios:

    p = usuario in A
    q = usuario in B
    r = usuario in C

    if usuario_critico(p, q, r):
        criticos.append(usuario)
    else:
        no_criticos.append(usuario)

print(f"\nUsuarios críticos:\n{criticos}")
print(f"\nUsuarios no críticos:\n{no_criticos}")

# PARTE C — INTERPRETACIÓN
print("\n********** PARTE C - INTERPRETACION **********")

# 8) RESPUESTAS
print("\n1) ¿Qué tipo de usuario representa mayor riesgo?")
print("Los usuarios críticos representan mayor riesgo")
print("porque utilizan la plataforma y además generan errores.")

print("\n2) ¿Qué significa que un usuario esté en C pero no en A ∪ B?")
print("Significa que generó errores pero no figura")
print("como usuario registrado en API o WEB.")

print("\n3) ¿Qué decisión tomaría el equipo programador?")
print("- Revisar logs del sistema")
print("- Auditar accesos")
print("- Mejorar validaciones")
print("- Monitorear usuarios críticos")
print("- Investigar usuarios desconocidos")
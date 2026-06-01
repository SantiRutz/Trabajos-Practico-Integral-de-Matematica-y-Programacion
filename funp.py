import math

def A(x):
    return 40 * x + 200

def B(x):
    return 70 * x + 50

def C(x):
    return -2 * (x ** 2) + 80 * x + 100

# ---------- PARTE A ----------
print("********** PARTE A — ANÁLISIS MATEMÁTICO **********")

# 1) Pendiente y ordenada
pendiente_A = 40
ordenada_A = 200
pendiente_B = 70
ordenada_B = 50
print("\n1) Pendiente y ordenada al origen")
print(f"A: pendiente = {pendiente_A}, ordenada = {ordenada_A}")
print(f"B: pendiente = {pendiente_B}, ordenada = {ordenada_B}")

# 2) ¿Son paralelas?
print("\n2) ¿Son paralelas?")
if pendiente_A == pendiente_B:
    print("Sí, son paralelas.")
else:
    print("No son paralelas.")

# 3) Intersección A y B
print("\n3) Intersección entre A y B")
x_inter = (ordenada_A - ordenada_B) / (pendiente_B - pendiente_A)
y_inter = A(x_inter)
print(f"Se cruzan en x = {x_inter}, y = {y_inter}")

# 4) Función C: vértice y raíces
print("\n4) Análisis de C(x) = -2x² + 80x + 100")
a, b, c = -2, 80, 100
xv = -b / (2 * a)
yv = C(xv)
print(f"Vértice: ({xv}, {yv})")

discriminante = b**2 - 4*a*c
if discriminante >= 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
    print(f"Raíces: {raiz1:.2f} y {raiz2:.2f}")
else:
    print("No tiene raíces reales.")

# Evaluación simple
valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]
print("\nEvaluación básica:")
for x in valores:
    print(f"x={x:2d} -> A={A(x):6.1f}, B={B(x):6.1f}, C={C(x):6.1f}")
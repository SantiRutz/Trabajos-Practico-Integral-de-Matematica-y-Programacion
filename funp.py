import math
import matplotlib.pyplot as plt

# FUNCIONES
def A(x):
    return 40 * x + 200 # 𝐴(𝑥) = 40𝑥 + 200
def B(x):
    return 70 * x + 50 # 𝐵(𝑥) = 70𝑥 + 50
def C(x):
    return -2 * (x ** 2) + 80 * x + 100 # 𝐶(𝑥) = −2𝑥² + 80𝑥 + 100

print("********** PARTE A — ANÁLISIS MATEMÁTICO **********") # PARTE A — ANÁLISIS MATEMÁTICO

# 1) Pendiente y ordenada al origen
pendiente_A = 40
ordenada_A = 200
pendiente_B = 70
ordenada_B = 50

print("\n1) PENDIENTE Y ORDENADA AL ORIGEN")
print(f"A(x) = 40x + 200", (f"\nPendiente de A: {pendiente_A}"))
print(f"Ordenada al origen de A: {ordenada_A}\n", (f"\nB(x) = 70x + 50"))
print(f"Pendiente de B: {pendiente_B}", (f"\nOrdenada al origen de B: {ordenada_B}"))

# 2) Paralelismo
print("\n2) ¿SON PARALELAS?")

if pendiente_A == pendiente_B:
    print("Las rectas SON paralelas.")
else:
    print("Las rectas NO son paralelas.")

# 3) Punto de intersección entre A y B
print("\n3) PUNTO DE INTERSECCIÓN ENTRE A Y B")

x_inter = (ordenada_A - ordenada_B) / (pendiente_B - pendiente_A)
y_inter = A(x_inter)

print(f"x = {x_inter}")
print(f"y = {y_inter}")

# 4) Función 
print("\n4) ANÁLISIS DE LA FUNCIÓN C")

# Vértice
a = -2
b = 80
c = 100
xv = -b / (2 * a)
yv = C(xv)

print("\nVÉRTICE") # Vértices
print(f"xv = {xv}")
print(f"yv = {yv}")
print("\nRAÍCES") # Raíces

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)

    print(f"Raíz 1 = {raiz1}")
    print(f"Raíz 2 = {raiz2}")
else:
    print("La función no tiene raíces reales.")

print("\n********** PARTE B — IMPLEMENTACIÓN **********") # PARTE B — IMPLEMENTACIÓN

# 7) Evaluar funciones
print("\n7) EVALUACIÓN DE FUNCIONES")

valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]

print("\n{:<10} {:<15} {:<15} {:<15}".format("x", "A(x)", "B(x)", "C(x)"))

for x in valores:
    print("{:<10} {:<15} {:<15} {:<15}".format(x, A(x), B(x), C(x)))

# 8) Plan más económico
print("\n8) PLAN MÁS ECONÓMICO")

def plan_mas_barato(x):
    costos = {
        "Plan A": A(x),
        "Plan B": B(x),
        "Plan C": C(x)
    }
    minimo = min(costos.values())

    mejores = []

    for plan, costo in costos.items():
        if costo == minimo:
            mejores.append(plan)
    return mejores, minimo

for x in valores:
    planes, costo = plan_mas_barato(x)
    print(f"\nCuando x = {x} horas:")
    print(f"El Plan más económico es: {planes}")
    print(f"Costo mínimo: {costo}")

print("\n********** PARTE C — ANÁLISIS **********") # PARTE C — ANÁLISIS

# 9) Determinar qué plan conviene
print("\n9) ¿QUÉ PLAN CONVIENE?")

for x in valores:
    planes, costo = plan_mas_barato(x)
    print(f"Para las {x} horas conviene el {planes} con costo de: {costo}")

# 10) Valores negativos de C
print("\n10) COSTOS NEGATIVOS EN C")

negativos = []

for x in range(0, 51):
    valor = C(x)

    if valor < 0:
        negativos.append((x, valor))

if negativos:
    print("\nValores donde C(x) es negativo:")
    for x, valor in negativos:
        print(f"x = {x} ---> C(x) = {valor}")
else:
    print("No hay valores negativos en el dominio.")

print("\nEXPLICACIÓN:") # Explicación del problema real
print("Un costo negativo significa que la empresa estaría pagando al cliente en lugar de cobrarle. \nEso representa un problema real porque:\n \n- La empresa tendría pérdidas económicas. \n- El modelo matemático deja de ser válido para ciertos valores. \n- En un sistema real no puede existir un costo negativo.\n \nPor eso es importante analizar el dominio y validar los resultados obtenidos por las funciones.\n")

# 6) Graficar funciones
x_vals = list(range(0, 51))

yA = [A(x) for x in x_vals]
yB = [B(x) for x in x_vals]
yC = [C(x) for x in x_vals]

plt.figure(figsize=(12, 6))
plt.plot(x_vals, yA, label="A(x) = 40x + 200")
plt.plot(x_vals, yB, label="B(x) = 70x + 50")
plt.plot(x_vals, yC, label="C(x) = -2x² + 80x + 100")
plt.title("Análisis de Costos de Desarrollo")
plt.xlabel("Horas mensuales")
plt.ylabel("Costo")
plt.grid(True)
plt.legend()
plt.show()
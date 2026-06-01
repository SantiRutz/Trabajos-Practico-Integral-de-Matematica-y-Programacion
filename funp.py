import math

def A(x):
    return 40 * x + 200

def B(x):
    return 70 * x + 50

def C(x):
    return -2 * (x ** 2) + 80 * x + 100

print("********** PARTE A — ANÁLISIS MATEMÁTICO **********")

# (Todo el análisis matemático de v2 se mantiene aquí...)
pendiente_A, ordenada_A = 40, 200
pendiente_B, ordenada_B = 70, 50
print("\n1) Pendiente y ordenada al origen")
print(f"A: pendiente {pendiente_A}, ordenada {ordenada_A}")
print(f"B: pendiente {pendiente_B}, ordenada {ordenada_B}")

print("\n2) ¿Son paralelas?")
print("No son paralelas." if pendiente_A != pendiente_B else "Sí son paralelas.")

x_inter = (ordenada_A - ordenada_B) / (pendiente_B - pendiente_A)
y_inter = A(x_inter)
print(f"\n3) Intersección A y B: x = {x_inter}, y = {y_inter}")

a, b, c = -2, 80, 100
xv = -b / (2*a)
yv = C(xv)
print(f"\n4) Vértice de C: ({xv}, {yv})")
discriminante = b**2 - 4*a*c
raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
print(f"Raíces de C: {raiz1:.2f}, {raiz2:.2f}")

print("\n********** PARTE B — COMPARACIÓN DE PLANES **********")

# Función para encontrar el plan más barato
def plan_mas_barato(x):
    """
    Devuelve el/los planes con menor costo para un valor de x dado.
    Retorna una tupla (planes, costo_minimo)
    """
    costos = {
        'A': A(x),
        'B': B(x),
        'C': C(x)
    }
    
    costo_minimo = min(costos.values())
    planes_minimos = [plan for plan, costo in costos.items() if costo == costo_minimo]
    
    return planes_minimos, costo_minimo

# Evaluación de los nueve valores solicitados
valores = [0, 5, 10, 15, 20, 25, 30, 40, 50]

print("\n1) Tabla de comparación de costos para cada plan:")
print("-" * 65)
print(f"{'x':<6} {'Plan A':<12} {'Plan B':<12} {'Plan C':<12} {'Mejor Plan':<15}")
print("-" * 65)

mejores_planes = {}
for x in valores:
    costo_a = A(x)
    costo_b = B(x)
    costo_c = C(x)
    
    planes_baratos, costo_min = plan_mas_barato(x)
    mejores_planes[x] = (planes_baratos, costo_min)
    
    planes_str = "/".join(planes_baratos)
    print(f"{x:<6} ${costo_a:<11.2f} ${costo_b:<11.2f} ${costo_c:<11.2f} {planes_str} (${costo_min:.2f})")

print("\n2) Resumen: Plan más económico para cada valor de x")
print("-" * 50)
for x in valores:
    planes, costo = mejores_planes[x]
    planes_str = " o ".join(["Plan " + p for p in planes])
    print(f"x = {x:2d} unidades → {planes_str:20} | ${costo:7.2f}")
import numpy as np

# MATRICES
M = np.array([
    [120, 150, 100],
    [200, 180, 220],
    [90, 110, 95]
])

C = np.array([
    [30, 20, 10],
    [15, 25, 20],
    [40, 10, 30]
])

print("\n********** PARTE A — COMPRENSIÓN DEL MODELO **********")
print("\n1) INTERPRETACIÓN")
print("\nCada fila de M representa una función del sistema.")
print("Fila 1 -> Autenticación")
print("Fila 2 -> Procesamiento de datos")
print("Fila 3 -> Generación de reportes")
print("Cada columna representa un servidor distinto.")
print("Columna 1 -> Servidor 1")
print("Columna 2 -> Servidor 2")
print("Columna 3 -> Servidor 3")
print("Cada valor representa el tiempo promedio de ejecución de una función en un servidor específico.")

print("\n2) DIMENSIONES")
filas_M, columnas_M = M.shape
filas_C, columnas_C = C.shape
print(f"\nM tiene dimensión: {filas_M}x{columnas_M}")
print(f"C tiene dimensión: {filas_C}x{columnas_C}")

if columnas_M == filas_C:
    print("\nSe puede calcular M * C")
    print("\nPorque el número de columnas de M")
    print("es igual al número de filas de C")
else:
    print("\nNO se puede calcular M * C")

# PARTE B — IMPLEMENTACIÓN (parcial)
print("\n********** PARTE B — IMPLEMENTACIÓN **********")
print("\n3) PROMEDIOS")

# Promedio por función (filas)
promedio_funciones = np.mean(M, axis=1)
print("\nTiempo promedio por función:")
for i, promedio in enumerate(promedio_funciones, start=1):
    print(f"Función {i}: {promedio:.2f} ms")

# Promedio por servidor (columnas)
promedio_servidores = np.mean(M, axis=0)
print("\nTiempo promedio por servidor:")
for i, promedio in enumerate(promedio_servidores, start=1):
    print(f"Servidor {i}: {promedio:.2f} ms")
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

# PARTE B — IMPLEMENTACIÓN
print("\n********** PARTE B — IMPLEMENTACIÓN **********")
print("\n3) PROMEDIOS")
promedio_funciones = np.mean(M, axis=1)
print("\nTiempo promedio por función:")
for i, promedio in enumerate(promedio_funciones, start=1):
    print(f"Función {i}: {promedio:.2f} ms")

promedio_servidores = np.mean(M, axis=0)
print("\nTiempo promedio por servidor:")
for i, promedio in enumerate(promedio_servidores, start=1):
    print(f"Servidor {i}: {promedio:.2f} ms")

# 4) Transpuesta
print("\n4) MATRIZ TRANSPUESTA")
M_transpuesta = M.T
print("\nMatriz transpuesta:")
print(M_transpuesta)
print("\nLa matriz transpuesta intercambia filas por columnas.")
print("Ahora:")
print("- Las filas representan servidores")
print("- Las columnas representan funciones")

# PARTE C — PRODUCTO MATRICIAL
print("\n********** PARTE C — PRODUCTO MATRICIAL **********")
print("\n5) T = M * C")
T = np.dot(M, C)
print(f"\nMatriz T:\n{T}")

# PARTE D — INTERPRETACIÓN CRÍTICA
print("\n********** PARTE D — INTERPRETACIÓN CRÍTICA **********")
print("\n6) INTERPRETACIÓN DE T")
print("\nCada valor de T combina tiempos promedio y cantidades de ejecuciones mediante multiplicación matricial.")
print("Puede interpretarse como una medida combinada de carga computacional.")
print("\nSin embargo, el producto matricial no representa directamente una magnitud física clara en este contexto.")

print("\n7) ALTERNATIVA MÁS ADECUADA")
print("\nUna alternativa más correcta sería realizar multiplicación elemento a elemento.")
print("De esta manera: Tiempo total = tiempo promedio * cantidad de ejecuciones para cada función y servidor.")
total_real = M * C
print("\nMultiplicación elemento a elemento:")
print(total_real)
print("\nEsto representa el tiempo total consumido por cada función en cada servidor.")
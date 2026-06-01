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

print("Matriz M (tiempos promedio):")
print(M)
print("\nMatriz C (cantidad de ejecuciones):")
print(C)

# Exploración de dimensiones
print("\nDimensiones:")
print(f"M: {M.shape}")
print(f"C: {C.shape}")
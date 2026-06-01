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
print("\n1) INTERPRETACIÓN") # 1) Interpretación

print("\nCada fila de M representa una función del sistema. \nFila 1 -> Autenticación \nFila 2 -> Procesamiento de datos \nFila 3 -> Generación de reportes \nCada columna representa un servidor distinto. \nColumna 1 -> Servidor 1 \nColumna 2 -> Servidor 2 \nColumna 3 -> Servidor 3 \nCada valor representa el tiempo promedio de ejecución de una función en un servidor específico.")

print("\n2) DIMENSIONES") # 2) Dimensiones y producto matricial

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

# 3) Promedios
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

# 4) Transpuesta
print("\n4) MATRIZ TRANSPUESTA")

M_transpuesta = M.T

print("\nMatriz transpuesta:")
print(M_transpuesta)

print("\nLa matriz transpuesta intercambia filas por columnas. \nAhora: \n- Las filas representan servidores \n- Las columnas representan funciones")

# PARTE C — PRODUCTO MATRICIAL
print("\n********** PARTE C — PRODUCTO MATRICIAL **********")

# 5) Producto matricial
print("\n5) T = M * C")

T = np.dot(M, C)

print(f"\nMatriz T: \n {T}")

print("\n********** PARTE D — INTERPRETACIÓN CRÍTICA **********") # PARTE D — INTERPRETACIÓN CRÍTICA

# 6) Interpretación
print("\n6) INTERPRETACIÓN DE T")

print("\nCada valor de T combina: \n- tiempos promedio \n- cantidades de ejecuciones \nmediante multiplicación matricial. \nPuede interpretarse como una medida combinada de carga computacional.")

print("\nSin embargo, el producto matricial no representa directamente una magnitud física clara en este contexto.")

# 7) Alternativa
print("\n7) ALTERNATIVA MÁS ADECUADA")

print("\nUna alternativa más correcta sería realizar multiplicación elemento a elemento. \nDe esta manera: \nTiempo total = tiempo promedio * cantidad de ejecuciones \npara cada función y servidor.")

# Multiplicación elemento a elemento
total_real = M * C

print("\nMultiplicación elemento a elemento:")
print(total_real)

print("\nEsto representa el tiempo total consumido por cada función en cada servidor.")

# PARTE E — PROPIEDADES
print("\n********** PARTE E — PROPIEDADES DE LA MATRIZ **********")

# 8) Simetría
print("\n8) MATRIZ SIMÉTRICA")

if np.array_equal(M, M.T):
    print("\nLa matriz M es simétrica")
else:
    print("\nLa matriz M NO es simétrica")

# 9) Invertibilidad
print("\n9) MATRIZ INVERTIBLE")

determinante = np.linalg.det(M)

print(f"\nDeterminante = {determinante:.2f}")

if determinante != 0:
    print("\nLa matriz es invertible")

    inversa = np.linalg.inv(M)

    print("\nMatriz inversa:")
    print(inversa)

else:
    print("\nLa matriz NO es invertible")

# 10) Interpretación
print("\n10) INTERPRETACIÓN")

print("\nSi la matriz no fuera invertible: \n- Habría información redundante \n- Algunas filas o columnas dependerían de otras \n- No sería posible recuperar información original \n- El sistema tendría dependencia lineal")

# PARTE F — ANÁLISIS APLICADO
print("\n ********** PARTE F — ANÁLISIS APLICADO **********")

# 11) Mayor costo y servidor eficiente
print("\n11) ANÁLISIS")

funcion_mayor_costo = np.argmax(promedio_funciones) + 1
servidor_mas_eficiente = np.argmin(promedio_servidores) + 1

print(f"\nLa función con mayor costo es la función {funcion_mayor_costo}")
print(f"El servidor más eficiente es el servidor {servidor_mas_eficiente}")

# 12) Recomendación técnica
print("\n12) RECOMENDACIÓN TÉCNICA")

print("\nSe recomienda: \n- Optimizar la función con mayor tiempo promedio \n- Redistribuir carga hacia el servidor más eficiente \n- Analizar cuellos de botella \n- Balancear las ejecuciones entre servidores \n- Implementar monitoreo continuo de rendimiento")
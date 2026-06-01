def A(x):
    return 40 * x + 200

def B(x):
    return 70 * x + 50

def C(x):
    return -2 * (x ** 2) + 80 * x + 100

# Evaluación para algunos valores
valores = [0, 5, 10, 15, 20]
print("x   |   A(x)   B(x)   C(x)")
print("----------------------------")
for x in valores:
    print(f"{x:<3} | {A(x):<7} {B(x):<7} {C(x):<7}")
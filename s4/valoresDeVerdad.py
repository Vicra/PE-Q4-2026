# VALORES DE VERDAD - TIPOS DE DATOS
print("1")
print(1)
print(int("1"))
print(float("1"))
print(bool("1"))
print(bool("perro"))
print(bool(""))
print("Cero:", bool(0))
print("Negativo:", bool(-10))

x = 4
print("A", 0 or x>3)
y = 2
print("B", bool(0 and y<3))
print("C", bool('c' or ""))
print(bool(2.5))
print("Arreglo vacio:", bool([]))
print("Arreglo:", bool([1, 2, 3]))



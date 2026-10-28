nombres = ["Andrea", "Esther", "Carolina", "Marvin"]
# leer el elemento en la posicion 0
# print(nombres[0])

# se lee como: muestre el elemento en la posicion 3
# print(nombres[3])

# no deberia de funciona pero asaber pq muestra el ultimo
# print(nombres[-1])

print("\n=====NOMBRES====")

# i inicia en 0
# en cada iteracion se pregunta si i < fin (es el segundo parametro)
# si la prosicion es verdadera se ejecuta lo que esta dentro del ciclo
# sino se sale del ciclo

# PRUEBA DE ESCRITORIO
# 0 < 4? -> SI
# 1 < 4? -> SI
# 2 < 4? -> SI
# 3 < 4? -> SI
# 4 < 4? -> NO
for i in range(0, 4):
  print(nombres[i])

# es lo mismo de arriba
# for index in range(0, 4):
#  print(nombres[index])

# ejemplo de iteraciones sobre cualquier rango
for goku in range(3, 8):
  print("Valor del indice: ", goku)

calificaciones = [70.23, 56.9, 86.4]

# len(lista)
# es una funcion que retorna el tamaño(cantidad de elementos)
# en una coleccion o lista
for index in range(0, len(calificaciones)):
  print(calificaciones[index])


for i in range(0, 5):
  print("*")

for i in range(0,5):
  for j in range(0, i):
    print("*", end="")
  print("")
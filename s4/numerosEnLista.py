numeros = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# n = 10

# mostrar todos los numeros de la serie print()
# for [var] in range(min, max):

for i in range(0, len(numeros)):
  print(f"{numeros[i]}", end=" ")

# i = 0, 0 < 9 ? si.  i = i + 1 -> 1
# i = 1, 1 < 9 ? si.  i = 1 + 1 -> 2
# i = 2, 2 < 9 ? si.  i = 2 + 1 -> 3
# i = 3, 3 < 9 ? si.  i = 3 + 1 -> 4
# ...
# i = 8, 8 < 9 ? si.  i = 8 + 1 -> 9
# i = 9, 9 < 9 ? NO.
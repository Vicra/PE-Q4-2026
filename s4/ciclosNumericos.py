# Ejercicio 1
# Mostrar numeros del 1-100 con un ciclo (for o while)

# 1.A while
num = 1
print("\nIMPRIMIR CON WHILE")
while (num <= 100):  
  # imprimir con formatting con un string empotrado (embedded)
  # f significa format
  print(f"{num} ", end="")
  num = num + 1
print("Fuera del while")
# ir sumando

# 1.B for
# sintaxis: for [var] in range(min, max)
# var = min
# while(var < max)

print("\nIMPRIMIR CON FOR")
for i in range(1, 101):
  # end="" esto sustituye imprimir un newline(enter) despues de imprimir
  print(i, end=" ")
  # esto es lo mismo de la linea 23
  # print(i, " ", end="")
number = 7
guess = -1

# ciclo infinito
while(True):
  guess = int(input("Adivine un numero entre 1-10: "))
  if(number == guess):
    print("Correcto")
    break
  else:
    print("Intente de nuevo")

print("Fuera del while")
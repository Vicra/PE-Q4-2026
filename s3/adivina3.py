# paquete/libreria de generacion de numero aleatorios
import random

# funcion para generacion en base a rango, incluyente
secret = random.randint(1, 10)

guess = -1
while(True):
  guess = int(input("Adivina un numero entre 1-10: "))
  if(guess != secret):
    print("Intente de nuevo")
  else:
    print("Correcto")
    break

print("Fin del while Adios!")
number = 7
# valor por defecto para inicializar 'guess' y poder
# ejecutar el primer ciclo
guess = -1

while(number != guess):
  guess = int(input("Adivine un numero entre 1-10: "))
  if(number == guess):
    print("Correcto")
  else:
    print("Intente de nuevo")

print("Fuera del while")
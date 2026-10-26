while True:
  print("MENU")
  print("1. Sumar")
  print("2. Restar")
  print("3. Multiplicar")
  print("4. Dividir")
  print("0. SALIR DEL SISTEMA")
  option = int(input("Ingrese una opcion:"))

  if(option < 0 or option > 4):
    print("Opcion no valida")
  else:
    x = int(input("Ingrese el valor de x:"))
    y = int(input("Ingrese el valor de y:"))

  if(option == 1):
    z = x + y
    print("La suma de 'x' y 'y' es :", z)
  elif(option == 2):
    z = x - y
    print("La resta de 'x' y 'y' es :", z)
  elif(option == 3):
    z = x * y
    print("La mult de 'x' y 'y' es :", z)
  elif(option == 4):
    z = x / y
    print("La div de 'x' y 'y' es :", z)
  elif(option == 0):
    print("BYEEE!")
    break
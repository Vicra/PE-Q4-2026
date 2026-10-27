option = ""
while(option != "Z"):
  print("---------")
  print("MENU")
  print("A. Sumar")
  print("B. Restar")
  print("C. Multiplicar")
  print("Z. SALIR") 

  option = input("Ingrese una opcion: ")
  # convertir de minusculas a mayusculas
  option = option.upper()

  # switch statement
  match(option):
    case "A":
      x = int(input("Ingrese el valor de x"))
      y = int(input("Ingrese el valor de y"))
      res = x + y
      print("Res:", res)
    case "B":
      x = int(input("Ingrese el valor de x"))
      y = int(input("Ingrese el valor de y"))
      res = x - y
      print("Res:", res)
    case "Z":
      print("Saliendo del sistema...")
    # default case
    case _:
      print("Opcion no valida")

print("Fuera del while")


# ejemplos
# "z" -> upper() -> "Z"
# "Z " == "Z" ? -> True
carreras = {
  "I1": "Ing sistemas",
  "I2": "Ing Civil",
  "I3": "Ing Mecatronica"
}

materias = {
  "M1": {
    "codigo": "PRO1",
    "nombre": "Programacion 1",
    "carrera": "I1"
  },
  "M2": {
    "codigo": "PRO2",
    "nombre": "Programacion 2",
    "carrera": "I1"
  },
  "M3": {
    "codigo": "TOP1",
    "nombre": "Topografia 1",
    "carrera": "I2"
  },
  "M4": {
    "codigo": "TOP2",
    "nombre": "Topografia 2",
    "carrera": "I2"
  }
}

def agregar_carrera():
  # agregar carrera
  codigo = input("Ingrese el codigo de la carrera: ")
  nombre = input("Ingrese el nombre de la carrera: ")

  # verificar que el codigo no exista
  codigoDuplicado = False
  for key in carreras.keys():
    if key == codigo:
      codigoDuplicado = True

  if codigoDuplicado == True:
    print("No se puede crear una carrera con un codigo ya existente")
  else:
    carreras[codigo] = nombre

def obtainNumber(message):
  while(True):
    numero = input(message)
    try:
      int(numero)
    except:
      print("\nERROR: Valor ingresado no es un numero entero")
      continue
    return int(numero)

def mostrar_menu_principal():
  option = -1
  while(option != 0):
    print("\n=====MENU=====")
    print("1. Gestionar Carreras")
    print("2. Gestionar Materias")
    # ...
    print("0. SALIR")

    option = obtainNumber("Ingrese una opcion: ")

    match option:
      case 1:
        mostrar_menu_carreras()
      case 0:
        print("Saliendo del sistema...")

def mostrar_menu_carreras():
  option = -1
  while(option != 0):
    print("\n==== GESTION DE CARRERAS - MENU ======")
    print("1. Mostrar Carreras")
    print("2. Crear Carrera")
    print("3. Borrar Carrera")
    print("4. Buscar Carrera")
    print("0. Regresar al menu principal")

    option = obtainNumber("Ingrese una opcion: ")

    match option:
      case 1:
        mostrar_carreras()
      case 2:
        agregar_carrera()
      case 3:
        borrar_carrera()
      case 0:
        print("\nSaliendo del submenu...")

def borrar_carrera():
  mostrar_carreras()
  codigoAborrar = input("Ingrese el codigo de la carrera que desea borrar:")

  # validar si tiene info relacionada
  hayRelacion = False
  for value in materias.values():
    if value["carrera"] == codigoAborrar:
      hayRelacion = True
      break
  if hayRelacion == True:
    print("No puede borrar una carrera relacionada con materias")
  else:
    carreras.pop(codigoAborrar)
    print("Se elimino la carrera:", codigoAborrar)
  

def mostrar_carreras():
  print("\n===CARRERAS===")
  for key, value in carreras.items():
    print(f"{key} - {value}")

mostrar_menu_principal()
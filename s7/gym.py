idSequence = 2
spaces = [
  "Piscina",
  "Cancha de Tennis",
  "Cancha de Futbol",
  "Cancha de Basquet"
]

days = [
  "Domingo", "Lunes", "Martes", 
  "Miercoles", "Jueves", "Viernes", "Sabado"
]
option = -1

reservations = {
  "R1": {
    "name": "Robert Pattison",
    "space": "Cancha de Basquet",
    "day":"Viernes",
    "peopleCount": 3
  }
}


def showDays():
  print("\n=====DAYS====")
  for i in range(len(days)):
    print(f"{i+1}. {days[i]}")

def showSpaces():
  print("\n=======SPACES======")
  for i in range(len(spaces)):
    print(f"{i+1}. {spaces[i]}")

def obtainName():
  name = ""
  while(name == ""):
    name = input("Ingrese el nombre: ")
    if(name == ""):
      print("\nERROR: El nombre no puede ser vacio.")
  return name

def obtainNumber(message):
  while(True):
    numero = input(message)
    try:
      int(numero)
    except:
      print("\nERROR: Valor ingresado no es un numero")
      continue
    return int(numero)

while(option != 0):
  print("\n======MENU=====")
  print("1. Registrar reserva")
  print("2. Mostrar reservas")

  option = int(input("Ingrese una opcion: "))

  match option:
    case 1:
      name = obtainName()
      showSpaces()
      spaceIndex = obtainNumber("Ingrese el numero del espacio: ")
      # syntax sugar de linea 27
      # spaceIndex -= 1
      spaceIndex = spaceIndex - 1
      while(spaceIndex < 0 or spaceIndex > len(spaces)):
        print("Not valid input\n")
        showSpaces()
        spaceIndex = obtainNumber("Ingrese el numero del espacio: ")
        spaceIndex = spaceIndex - 1

      showDays()
      day = obtainNumber("Ingrese el dia de la reserva: ")
      day = day -1

      peopleCount = 0
      while(peopleCount <= 0):
        peopleCount = obtainNumber("Ingrese la cantidad de personas: ")
        if (peopleCount <= 0):
          print("\nERROR: Cantidad de personas no puede ser menor que 1")



      # validaciones
      # 1 validacion: No puede reservar dos espacio el mismo dia, la misma persona
      hasReservationOnSameDay = False
      for key, value in reservations.items():
        if name == value["name"] and days[day] == value["day"]:
          hasReservationOnSameDay = True
          # me salgo del ciclo porque ya encontre un match de doble reservation
          break
      if hasReservationOnSameDay == True:
        print("No se puede agregar dos reservaciones en el mismo dia")
      else: 
        # equivalent a append() en list
        reservations["R" + str(idSequence)] = {
          "name": name,
          "space": spaces[spaceIndex],
          "day": days[day],
          "peopleCount": peopleCount
        }
        # idSequence += 1
        idSequence = idSequence + 1
    case 2:
      # foreach
      print("\n======RESERVATIONS======")
      for key, value in reservations.items():
        print(f"{key} - {value["name"]} - {value["space"]} - {value["day"]} - {value["peopleCount"]}")
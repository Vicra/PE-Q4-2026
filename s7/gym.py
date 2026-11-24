idSequence = 1
spaces = [
  "Piscina",
  "Cancha de Tennis",
  "Cancha de Futbol",
  "Cancha de Basquet"
]

days = [
  "Dom", "Lun", "Mart", "Mierc", "Juev", "Viern"
]
option = -1

reservations = {}


def showDays():
  print("\n=====DAYS====")
  for i in range(days):
    print(f"{days[i]}")

def showSpaces():
  print("\n=======SPACES======")
  for i in range(len(spaces)):
    print(f"{i+1}. {spaces[i]}")

while(option != 0):
  print("\n======MENU=====")
  print("1. Registrar reserva")
  print("2. Mostrar reservas")

  option = int(input("Ingrese una opcion: "))

  match option:
    case 1:
      name = input("Ingrese el nombre: ")
      showSpaces()
      spaceIndex = int(input("Ingrese el numero del espacio: "))
      # syntax sugar de linea 27
      # spaceIndex -= 1
      spaceIndex = spaceIndex - 1
      while(spaceIndex < 0 or spaceIndex > len(spaces)):
        print("Not valid input\n")
        showSpaces()
        spaceIndex = int(input("Ingrese el numero del espacio: "))
        spaceIndex = spaceIndex - 1

      showDays()
      day = int(input("Ingrese el dia de la reserva: "))
      peopleCount = int(input("Ingrese la cantidad de personas: "))

      # validaciones
      # 1 validacion: No puede reservar dos espacio el mismo dia, la misma persona
      hasReservationOnSameDay = False
      for key, value in reservations.items():
        if name == value["name"] and day == value["day"]:
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
          "day": day,
          "peopleCount": peopleCount
        }
        # idSequence += 1
        idSequence = idSequence + 1
    case 2:
      # foreach
      print("\n======RESERVATIONS======")
      for key, value in reservations.items():
        print(f"{key} - {value["name"]} - {value["space"]} - {value["day"]} - {value["peopleCount"]}")
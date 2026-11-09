# ambito global
tareas = []
estados = []

def agregar_tarea():
  nuevaTarea = input("Ingrese el nombre de la tarea: ")

  # agregar tareas a traves de append()
  # nombreDeLaLista.append(elem)
  tareas.append(nuevaTarea)

  # tarea con valor por defecto pendiente(false)
  estados.append(False)

# declaracion de la fn
def mostrar_tareas():
  print("\n===== LISTA DE TAREAS =====")
  for i in range(0, len(tareas)):
    print(f"{i+1}\t{tareas[i]}\t", end="")
    if(estados[i] == False):
      print("Pendiente")
    else:
      print("Completado")

def completar_tarea():
  mostrar_tareas()
  indice = int(input("Ingrese el indice de la tarea a completar: "))
  if(indice < 1 or indice > len(tareas)):
    print("Indice incorrecto, vuelva a intentarlo")
  else:
    indice = indice - 1
    estados[indice] = True

def mostrar_tareas_pendientes():
  contadorPendientes = 0
  print("===== TAREAS PENDIENTES =====")
  for i in range(0, len(tareas)):
    if (estados[i] == False):
      print(tareas[i])
      contadorPendientes = contadorPendientes + 1
  print("Total tareas pendientes:", contadorPendientes)

opcion = -1
while(opcion != 0):
  print("\n=======ADMINISTRADOR DE TAREAS======")
  print("1. Agregar tarea")
  print("2. Mostrar tareas")
  print("3. Completar una tarea")
  print("4. Mostrar tareas pendientes")
  print("0. Salir")
  # ...

  opcion = int(input("Ingrese una opcion: "))
  match opcion:
    case 0:
      print("Byee")
    case 1:
      agregar_tarea()
    case 2:
      mostrar_tareas()
    case 3:
      completar_tarea()
    case 4:
      mostrar_tareas_pendientes()
    case _:
      print("Opcion Invalida")
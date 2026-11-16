titles = ["Baby Wow", "Thriller", "Last Christmas"]
authors = ["KarolG", "MJ", "Wham"]
genres = ["Reggaeton", "Pop", "Balada"]
durations = [200, 220, 300]
years = [2026, 1980, 1990]

def imprimir_canciones():
  if(len(titles) == 0):
    print("No hay canciones")
  else:
    for i in range(len(titles)):
      print(f"{i+1}. {titles[i]}\t{authors[i]}")

def agregar_cancion():
  title = input("Ingrese el titulo:")
  titles.append(title)

  author = input("Ingrese el author:")
  authors.append(author)

  genre = input("Ingrese el genero:")
  genres.append(genre)

  duration = -1
  while(duration < 0):
    # append
    duration = int(input("Ingrese la duracion:"))

    if(duration < 0):
      print("Duracion no valida")
    
  durations.append(duration)

  year = 0
  while(year < 1900 or year > 2026):
    year = int(input("Ingrese el año:"))

    if(year < 1900 or year > 2026):
      print("Año no valido")
  
  years.append(year)

def borrar_cancion():
  imprimir_canciones()
  aBorrar = int(input("Ingrese el numero de cancion que desea borrar:"))
  # aBorrar = aBorrar - 1

  titles.pop(aBorrar - 1)
  authors.pop(aBorrar - 1)
  genres.pop(aBorrar - 1)
  durations.pop(aBorrar - 1)
  years.pop(aBorrar -1)

  # del years[aBorrar-1]
  # years.remove(years[aBorrar-1])


  print("Canciona borrada....\n")

def buscar_por_genero():
  genero = input("Ingrese el genero a buscar:")
  encontrado = False
  for i in range(len(genres)):
    if(genres[i].upper() == genero.upper()):
      encontrado = True
      print(f"{titles[i]}\t{genres[i]}")

  if(not encontrado): #if(encontrado == False):
    print("No se encontraron canciones con ese genero")

def mostrar_duracion_total():
  duracion = 0
  for i in range(len(durations)):
    # duracion = durations[i] + duracion
    duracion += durations[i]
  print("la duracion total es:", duracion)

option = -1
while(option != 0):
  print("MENU")
  print("1. Mostrar canciones")
  print("2. Agregar cancion")
  print("3. Borrar cancion")
  print("4. Buscar por genero")
  print("5. Duracion total")
  print("0. Salir")

  option = int(input("Ingrese una opcion:"))

  match option:
    case 1:
      imprimir_canciones()
    case 2:
      agregar_cancion()
    case 3:
      borrar_cancion()
    case 4:
      buscar_por_genero()
    case 5:
      mostrar_duracion_total()
    case 0:
      print("Byeee!!")
    case _:
      print("Opcion no valida")
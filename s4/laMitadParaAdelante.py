import math
alumnos = ["Ulises", "Walter", "Ana", 
           "Daniel", "Pablo", "Edwin", 
           "Andrea", "Esther", "Victor"]
# solo mostrar de la mitad para adelante
# hacer ejercicio con for

# Pablo, Edwin, Andrea, Esther
# mostrar desde la mitad hasta el inicio
for i in range(math.floor(len(alumnos)/2), len(alumnos)):
  print(alumnos[i], end=", ")

# mostrar desde el inicio hasta la mitad
for i in range(0, math.floor(len(alumnos)/2)):
  print(alumnos[i], end=", ")
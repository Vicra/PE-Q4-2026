import math
alumnos = ["Ulises", "Walter", "Ana", 
           "Daniel", "Pablo", "Edwin", 
           "Andrea", "Esther", "Victor"]
# solo mostrar de la mitad para adelante
# hacer ejercicio con for

# Pablo, Edwin, Andrea, Esther
for i in range(math.floor(len(alumnos)/2), len(alumnos)):
  print(alumnos[i], end=", ")
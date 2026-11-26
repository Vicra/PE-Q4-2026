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

# mostrar las carreras
for key, value in carreras.items():
  print(f"{key} - {value}")

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

# mostrar las carreras
for key, value in carreras.items():
  print(f"{key} - {value}")
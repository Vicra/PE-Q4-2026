numeros = {
  "numero1": 1,
  "numero2": 2
}

numeros = [1, 2, 3, 4]

alumnos = {
  "21311096": {
    "nombre": "Victor ",
    "apellidos": "Ramirez",
    "carrera": "Ing Sistemas"
  },
  "22641055": {
    "nombre": "Andrea",
    "apellidos": "Pineda",
    "carrera": "Ing Energia"
  },
  "22641056": {
    "nombre": "Esther",
    "apellidos": "Bueso",
    "carrera": "Ing Industrial"
  }
}

ordenes = {
  "1": {
    "fecha": "11/20/2026",
    "nombre": "Juan",
    "total": 100.34,
    "detalle":[
      {
        "id": 1,
        "nombre": "Pepsi personal 500ml",
        "cantidad": 3,
        "precio": 20,
        "subtotal": 60.0
      },
      {
        "id": 2,
        "nombre": "Coca-cola personal",
        "cantidad": 2,
        "precio": 21,
        "subtotal": 42.0
      }
    ]
  }
}

# devuelve un arreglo con todas las llaves
# print(alumnos.keys())

# devuelve un arreglo con todas los valores
# print(alumnos.values())

print("MOSTRAR ALUMNOS")
# foreach
# for value in alumnos.values():
#  print(f"{value["nombre"]} {value["apellidos"]} - {value["carrera"]}")
# print("")

for key, value in alumnos.items():
  print(f"{value["nombre"]} {value["apellidos"]} - {key} - {value["carrera"]}")
print("")


cuenta = input("Ingrese el numero de cuenta:")
nombre = input("Ingrese el nombre:")
apellido = input("Ingrese el apellido:")
carrera = input("Ingrese la carrera:")

# diccionario[llave]
# leer el valor de la llave -> print(diccionario[llave])
# asinar una nueva llave -> diccionario[llave] = 



# print(ordenes)

# combinacion llave y valor
# la llave es un indentificador unico

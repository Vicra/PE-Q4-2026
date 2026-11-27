wish_list = {
  "W001": {
      "nombre": "Laptop",
      "categoria": "Tecnología",
      "precio": 15000,
      "prioridad": "Alta",
      "estado": "Pendiente"
  },
  "W002": {
      "nombre": "Bicicleta",
      "categoria": "Deportes",
      "precio": 5000,
      "prioridad": "Media",
      "estado": "Pendiente"
  },
  "W003": {
      "nombre": "Audífonos",
      "categoria": "Tecnología",
      "precio": 1200,
      "prioridad": "Baja",
      "estado": "Comprado"
  }
}

# ===== MI WISH LIST =====

# 1. Agregar un deseo
# 2. Mostrar todos los deseos (por prioridad)
# 3. Buscar un deseo (por nombre o categoria)
# 4. Cambiar prioridad 
# 5. Marcar como comprado 
# 6. Eliminar un deseo 
# 7. Salir 

# Seleccione una opción:

def mostrar_deseos():
  print("===DESEOS===")
  for key, value in wish_list.items():
    print(f"{key} - {value["nombre"]} - {value["precio"]} - {value["prioridad"]}  - {value["estado"]}")

mostrar_deseos()
codigo = input("Ingrese el deseo que quiere cambiarle la prioridad: ")

print("Prioridades")
print("1. Alta")
print("2. Media")
print("3. Baja")
nuevaPrioridad = int(input("Ingrese la nueva prioridad: "))

if nuevaPrioridad == 1:
  wish_list[codigo]["prioridad"] = "Alta"
elif nuevaPrioridad == 2:
  wish_list[codigo]["prioridad"] = "Media"
else:
  wish_list[codigo]["prioridad"] = "Baja"

mostrar_deseos()
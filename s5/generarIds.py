# Generacion de Ids
ids = []

# 1er parte de funcion DEFINICION
# camelCase
# Description: Generar y retornar el nuevo id
def generarIdParaProductos():
  # 1er caso: cuando la lista esta vacia retorna 1
  if(len(ids) == 0):
    return 1
  # Primero: obtener el ultimo elem
  ultimo = ids[len(ids) - 1]
  # sumarle uno al ultimo de 
  return ultimo + 1

# esta es lo mismo de arriba pero con else
def generarIdParaProductos2():
  if(len(ids) == 0):
    return 1
  else:
    ultimo = ids[len(ids) - 1]
    return ultimo + 1

# 2da parte: LLAMADO DE LA FUNCION
primerId = generarIdParaProductos()
print("Id generado:", primerId)

# Agregar el id a la lista
ids.append(primerId)

print("Lista de ids:", ids)

segundoId = generarIdParaProductos()
print("Id generado:", segundoId)
ids.append(segundoId)

print("Lista de ids:", ids)


ids.append(generarIdParaProductos())
ids.append(generarIdParaProductos())
ids.append(generarIdParaProductos())
ids.append(generarIdParaProductos())
ids.append(generarIdParaProductos())

ids.remove(7)

ids.append(generarIdParaProductos())

print("Lista de ids:", ids)
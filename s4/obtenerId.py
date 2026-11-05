# Generacion de Ids
ids = []

# 1er parte de funcion DEFINICION
# camelCase
# Description: Generar y retornar el nuevo id
def generarIdParaProductos():
  # 1er caso: cuando la lista esta vacia retorna 1
  if(len(ids) == 0):
    return 1
  # TODO: 2do caso: cuando la lista no esta vacia

# 2da parte: LLAMADO DE LA FUNCION
primerId = generarIdParaProductos()
print("Id generado", primerId)

# Agregar el id a la lista
ids.append(primerId)

print(ids)
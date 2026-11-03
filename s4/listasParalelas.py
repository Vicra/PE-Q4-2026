# Lista de Productos
idProductos = [1, 2, 3]
nombresProductos = ["Laptop", "Mouse", "Teclado"]
categoriasProductos = ["Electronica", "Accesorios", "Accesorios"]
preciosProductos = [15500.00, 399.99, 499.99]
stockProductos = [10, 20, 30]
# FIN Lista de Productos

print("ID\tNOMBRE\tCATEGORIA\tPRECIO\tSTOCK")
for i in range(0, len(idProductos)):
  # print(idProductos[i], nombresProductos[i], categoriasProductos[i], preciosProductos[i], stockProductos[i])
  print(f"{idProductos[i]}\t{nombresProductos[i]}\t{categoriasProductos[i]}\t{preciosProductos[i]}\t{stockProductos[i]}")

# ------------------------
# Busqueda
encontro = False
busqueda = input("Ingrese el nombre del producto que busca: ")
for i in range(0, len(nombresProductos)):
  # convertir a mayusculas ambas para incrementar el porcentaje de 
  # encontrados
  if(nombresProductos[i].upper() == busqueda.upper()):
    encontro = True
    # mostrar el nombre y el precio
    print("Nombre: ", nombresProductos[i], " Precio:", preciosProductos[i])

if (encontro == False):
  print("No encontro ese producto")
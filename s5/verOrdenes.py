idOrdenDetalle=[1,1,1]
idProductoDetalle=[1, 2, 3]
nombreProductoDetalle=["laptop", "mouse", "teclado"]
cantidades=[2, 3, 4]
preciosUnitarios=[10.4, 34.5, 40.3]
subtotales=[20.8, 103.5, 161.2]

print("DETALLE DE PRODUCTOS")
total = 0
for i in range(0, len(idProductoDetalle)):
  print(f"{i+1} {nombreProductoDetalle[i]}", end="\t")
  print(f"{cantidades[i]}", end="\t")
  print(f"{preciosUnitarios[i]}", end="\t")
  print(f"{subtotales[i]}", end="\n")
  total = total + subtotales[i]

print("TOTAL", total)
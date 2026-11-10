candidatos = ["Planilla1", "Planilla2", "Planilla3"]
votos = [0,0,0]

cantidadVotantes = int(input("Ingrese la cantidad de votantes: "))

for i in range(0, cantidadVotantes):
  print("\n-----LISTA DE CANDIDATOS----")
  for j in range(0, len(candidatos)):
    print(f"{j+1} {candidatos[j]}")

  voto = int(input("Ingrese su voto: "))

  voto = voto-1

  votos[voto] = votos[voto] + 1

print(votos)
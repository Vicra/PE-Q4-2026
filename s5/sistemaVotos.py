import os

candidatos = ["Esther", "Carolina", "Miguel"]
votos = [0,0,0]

participantes = int(input("Cuantos participantes van a votar?: "))

def limpiar_consola():
  # 'nt' es para Windows, 'posix' para Linux/macOS
  os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_candidatos():
  print("\n===== CANDIDATOS ======")
  for i in range(len(candidatos)):
    print(f"{i+1}.- {candidatos[i]}")

def mostrar_votos():
  print("\n==== RESULTADOS ===")
  for i in range(len(candidatos)):
    # embedded string -> texto empotrado/embebido
    print(f"{candidatos[i]} {votos[i]}")

def mostrar_ganador():
  mayor = 0
  for i in range(1, len(votos)):
    if(votos[i] > votos[mayor]):
      mayor = i
  print("GANADOR:", candidatos[mayor])

# ciclo principal para ver cuantos votos se van a registrar
for i in range(1, participantes+1):
  # mostrar los candidatos
  # pedir el voto
  mostrar_candidatos()
  tuVoto = int(input("Cual es tu voto?: "))

  # obtener el indice a cual le voy a sumar un voto
  votoIndiceOg = tuVoto - 1

  # sumar el voto al acumulado de votos
  votos[votoIndiceOg] = votos[votoIndiceOg] + 1
  limpiar_consola()
  
mostrar_votos()
mostrar_ganador()
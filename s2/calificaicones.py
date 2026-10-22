import math
score = float(input("Ingrese la calificación: "))
if(score >= 64.5 and score < 65): 
  score = math.ceil(score)
# validaciones
if(score < 0 or score > 100): 
  print("Calificacion no valida")
elif(score >= 90): print("Excelente Aprobo")
elif(score >= 65): print("Aprobado")
else: print("Reprobado")

def calcular_resultado(operacion):
    altura = float(input("Digite su altura en centimetros: "))
    if operacion == 1:
      resultado = 56.2+1.41*(altura/2.54-60)
    elif operacion == 2:
      resultado = 53.1+1.36*(altura/2.54-60)
    return resultado

"""Calorías quemadas = (Tiempo actividad (min) * MET * Peso (Kg)) /200"""

def calcular_calorias(opera):
  tiempo_actividad = int(input("ingrese los minutos realizados en actividad fisica: "))
  peso = int(input("Escriba su peso actual en kg: "))
  if opera == 1:
    resul = (tiempo_actividad*MET*peso/200)
  elif opera == 2:
    resul = (tiempo_actividad*MET*peso/200)
  elif opera == 3:
    resul = (tiempo_actividad*MET*peso/200)
  elif opera == 4:
    resul = (tiempo_actividad*MET*peso/200)
  elif opera == 5:
    resul = (tiempo_actividad*MET*peso/200)
  return resul


print("============================================")
print("           CALCULADORA SALUDABLE           ")
print("             HOMBRES Y MUJERES           ")
print("============================================")

"""OBJETIVO Este reto tiene como objetivo que apliques todos los conceptos que hemos visto en las semanas 1 y 2, para ello debes solucionar un problema aplicando el proceso IDEAL y luego implementar la solución en Python, utilizando funciones, parámetros y una muy buena documentación del código.
Este proyecto debe ser implementado en Python"""

"""CONTEXTO: Estar en forma se ha vuelto un aspecto importante y cotidiano en nuestra sociedad hasta convertirse en un estilo de vida. Un aspecto importante para las personas que siguen este estilo de vida son los diferentes indicadores de su estado físico. (peso, grasa, calorías, entre otros). Por eso en este reto vamos a implementar algunas de las métricas mas utilizadas por la “gente fitness”"""

"""PESO IDEAL IBW
Diferentes expertos a través de los años han definido fórmulas para calcular el peso ideal de una persona. Una de las mas usadas es la del Dr. Miller que establece que el peso ideal para hombres y mujeres está dado por las fórmulas
Hombre = 56.2 +1.41*(Altura (cm)/2.54 -60)
Mujer = 53.1 +1.36 *(Altura (cm)/2.54 -60))"""

opcion = 0

while(opcion != 3):
  print("==============================")
  print("   INGRESE SU TIPO DE SEXO")
  print("==============================")
  print("1. Hombre")
  print("2. Mujer")
  print("3. Salir")
  print("==============================")
  opcion = int(input("Seleccione una opción: "))
  print("==============================")
  
  if opcion == 1:
    print("Usted es de sexo masculino")
    resultado = calcular_resultado(1)
    print("Su peso ideal (IBW)", resultado)
  elif opcion == 2:
    print("Usted es de sexo femenino")
    resultado = calcular_resultado(2)
    print("Su peso ideal (IBW)", resultado)
  elif opcion == 3:
    print("Saliendo de la aplicación")
  else:
    print("La opción no es valida")
  if calcular_resultado == 1 or 2:
    print("==============================")
    print("   CONOCE CALORIAS QUEMADAS ")
    print("        SEGÚN ACTIVIDAD")
    print("==============================")
    print("1. Caminar")
    print("2. Tenis")
    print("3. Montar bicicleta")
    print("4. Correr")
    print("5. Nadar")
    print("6. Salir")
    print("==============================")
    MET = int(input("Seleccione una opción MET: "))
    if MET == 1:
      print("La actividad que realizo fue caminar")
      resul = calcular_calorias(1)
      print("Las calorias quemadas fueron: ", resul)
    elif MET == 2:
      print("La actividad que realizo fue jugar tenis")
      resul = calcular_calorias(2)
      print("Las calorias quemadas fueron: ", resul)
    elif MET == 3:
      print("La actividad que realizo fue montar bicicleta")
      resul = calcular_calorias(3)
      print("Las calorias quemadas fueron: ", resul)
    elif MET == 4:
      print("La actividad que realizo fue correr")
      resul = calcular_calorias(4)
      print("Las calorias quemadas fueron: ", resul)
    elif MET == 5:
      print("La actividad que realizo fue nadar")
      resul = calcular_calorias(5)
      print("Las calorias quemadas fueron: ", resul)
    elif MET == 6:
      print("Saliendo de la aplicación")

  print("================================================")
  print("               Gracias por utilizar")
  print("                nuestra calculadora")
  print("                     saludable")
  print("================================================")
"""QUEMANDO CALORIAS:
Diferentes expertos a través de los años han definido fórmulas para calcular el peso ideal de una persona. Una de las mas usadas es la del Dr. Miller que establece que el peso ideal para hombres y mujeres está dado por las fórmulas
Calorías quemadas = (Tiempo actividad (min) * MET * Peso (Kg)) /200"""

"""VALORES DEL MET: 
• Caminar = 2
• Tenis = 5
• Montar en bicicleta = 14
• Correr = 6
• Nadar = 9.8"""

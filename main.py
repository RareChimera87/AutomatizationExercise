import time
import random
def Binarizador(number):
  Binarios = []
  NumeroInicial = number
  Numero = NumeroInicial

  for i in range(0 ,Numero) :
    Cociente = Numero // 2
    Residuo = Numero % 2
    Binarios.append(Residuo)
    Numero = Cociente
    i = i + 1
    if Cociente == 0 :
      break
  
  Binarios.reverse()


  return (Binarios)



def automan():
  iteraciones = 0
  vez = 0
  fallasG = 0

  f = open("log_operacion.txt", "a")
  f.write("\n")
  f.write("\n")
  f.write("*****************")
  f.write("La fecha de la prueba es: ")
  fecha = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  f.write(fecha)
  f.write("*****************")
  f.write("\n")
  while iteraciones < 8:
    activos = 0
    fallas = 0
    alertas = []
    f.write("Prueba Numero: ")
    f.write(str(iteraciones))
    f.write("\n")
    numero = random.randint(0, 255)
    f.write("El numero elegido es: ")
    f.write(str(numero))
    f.write("\n")
    binario = Binarizador(numero)
    f.write("El binario es: ")
    f.write(str(binario))
    f.write("\n")

    for i in range(0, len(binario)):
      actitud = "inactivo"
      print("************")
      print("Inciando Pruebas del sensor: ", i)
      f.write("Iniciando pruebas de sensor: ")
      f.write(str(i))
      f.write("\n")
      if i == 2 and binario[i] == 1:
        f.write("!!!!ALERTA: Temperatura fuera de rango")
        alertas.append("!!!!ALERTA: Temperatura fuera de rango")
        fallasG = fallasG + 1
        fallas = fallas + 1
        f.write("\n")
      elif vez == 0 and binario[vez] == 0 and i == 1 and binario[i] == 0:
        f.write("!!!!Falla: Tanque 1 sin datos de nivel")
        alertas.append("!!!!Falla: Tanque 1 sin datos de nivel")
        fallasG = fallasG + 1
        fallas = fallas + 1
        f.write("\n")
      elif i == 7 and binario[i] == 1:
        f.write("!!!!INTRUSION DETECTADA: Enviar equipo de seguirdad")
        alertas.append("!!!!INTRUSION DETECTADA: Enviar equipo de seguirdad")
        fallas = fallas + 1
        fallasG = fallasG + 1
        f.write("\n")
      print("Sensor actual: ", i)
      f.write("Sensor actual: ")
      f.write(str(i))
      f.write("\n")
      if binario[i] == 1:
        actitud = "activo"
        print("Estado del sensor actual: ", actitud)
      else:
        print("Estado del sensor actual: ", actitud)
      f.write("Estado del sensor actual: ")
      f.write(str(binario[i]))
      f.write("\n")
      print("************")
      if binario[i] == 1:
        activos = activos + 1

      vez = i

    iteraciones = iteraciones + 1
    print("Numero de sensores activos durante la prueba: ", activos)
    f.write("Sensores activos durante prueba: ")
    f.write(str(activos))
    f.write("\n")
    
    f.write("Numero de alertas generadas durantes esta prueba: ")
    f.write(str(fallas))
    f.write("\n")

    f.write("Alertas generadas: ")
    f.write(str(alertas))
    f.write("\n")

    f.write("--------------------------------------------\n")
    time.sleep(5)

  f.write("*****************")
  f.write("Alertas totales generadas: ")
  f.write(str(fallasG))
  f.write("*****************")
  f.write("\n")  
  f.write("*****************")
  f.write("Gracias por usar nuestro tester")
  f.write("*****************")
  f.write("\n")  
  f.write("\n")  
  f.close()
  print("Gracias por usar nuestro tester")
  print("Vea el archivo Log para ver resultados y fallas")
automan()
#Simular cajero automatico con saldo $1000
def cajeroAuto():
    saldo = 1000

    while True:
      print('1: Ingresar dinero')
      print('2: Retirar dinero')
      print('3: Mostrar dinero')
      print('4: Salir')
      opcion = int(input('Ingrese una opcion'))
      if(opcion==1):
          dineroIngresado= int(input('Ingrese el monto'))
          saldo+=dineroIngresado
      elif(opcion==2):
          dineroRetirado= int(input('Ingrese el monto'))
          saldo-=dineroRetirado
      elif(opcion==3):
        print('Su saldo es de: ' + str(saldo))
      else: break

cajeroAuto()


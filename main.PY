import random
import os
#1 Se ingresa por teclado la categoría de un socio del club deportivo y su antigüedad en años. Las
#  categorías posibles son A, B y C. Luego se desea saber si el socio ingresado tiene categoría A o su
#  antigüedad se encuentra entre los 10 y 20 años, en esos casos se pide mostrar un cartel que exprese
#  lo siguiente: “Socio vip”.
print("Ejercicio 1")
categoria = input("Ingrese la categoría del socio ").upper()
socioVip=False
while categoria !="A" and categoria != "B" and categoria!="C":
   categoria = input("La categoría es incorrecta ").upper()
if categoria=="A":
   socioVip=True
antiguedad = int(input("Ingrese la antigüedad en el club en años "))
if antiguedad<10 or antiguedad>20 or categoria!="A":
   socioVip=False
   print("Socio normal")
else:
   print("Socio Vip")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#2 Dadas las horas trabajadas y la categoría de un empleado. Calcular y mostrar el sueldo, sabiendo
#  que la pagada por categoría es: Categoría 1: $200, Categoría 2: $300, Categoría 3: $400. 
print("Ejercicio 2")
horas=int(input("Ingrese horas trabajadas "))
cat=int(input("Ingrese su categoría "))
sueldo=0
while cat < 1 or cat > 3:
   cat=int(input("Ingrese categoría correcta (de 1 al 3) "))
if cat ==1:
   sueldo=horas*200
elif cat ==2:
   sueldo=horas*300
elif cat ==3:
   sueldo=horas*400
print("Su sueldo es $",sueldo)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#3  Ingresar un número natural por teclado. Se desea saber y mostrar si es par o impar.
print("Ejercicio 3")
num=float(input("Ingrese número "))
if num%2==0:
   print("Es par")
else:
   print("No es par")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#4 Ingresar un número entero para saber si es divisible por 7 y es mayor a 40.
print("Ejercicio 4")
num1=int(input("Ingrese otro número "))
if num1%7==0:
   print("Es divisible por 7")
else:
   print("No es divisible por 7")
if num1>40:
   print("Es mayor a 40")
else:
   print("No es mayor a 40")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#5 Diseñar un programa que pida un número por teclado y luego imprima el número siguiente al ingresado.
print("Ejercicio 5")
numero=int(input("Ingrese otro número "))
numero=numero+1
print("El número siguiente es",numero)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#6 Hacer un programa que genere un número aleatorio del 0 al 200, lo muestre y luego calcule y muestre
#  el mismo número aumentado en un 30 %. (Para generar números aleatorios usar: random.randit. Esta
#  función se debe importar como: import .random
print("Ejercicio 6")
numAzar = random.randint(0, 200)
print("El número elegido es",numAzar)
numAzar=(numAzar*30)/100+numAzar
print("Y su potenciado es",numAzar)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#7 Hacer un programa que imprima el área y el perímetro de un rectángulo ingresando su base y altura.
print("Ejercicio 7")
base=float(input("Ingrese la base "))
altura=float(input("Ingrese la altura "))
perimetro=base*2+altura*2
area=base*altura
print("El perimetro del rectángulo es",perimetro,"centímetros")
print("El área del rectángulo es",area,"centímetros cuadrados")
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#8  Una empresa paga a sus empleados un adicional según la antigüedad en años que tenga en la misma,
#   de acuerdo a la siguiente escala:
# a. Nada por una antigüedad menor a 1 año
# b. 5% por una antiguedad entre 1 y 3 años
# c. 10% por una antiguedad entre 4 y 6 años
# d. 20% por una antigüedad mayor a 6 años.
#   Indicar el sueldo del empleado y el nuevo sueldo con el incremento
print("Ejercicio 8")
salario=float(input("Ingrese el sueldo del empleado "))
antiguo=int(input("Ingrese la antigüedad del empleado en años "))
while antiguo<0:
   antiguo=int(input("Ingrese una antigüedad válida "))
if antiguo >=1:
   if antiguo<=3:
      salario=(salario*5)/100+salario
      print("El sueldo del empleado es",salario)
   elif antiguo <=6:
      salario=(salario*10)/100+salario
      print("El sueldo del empleado es",salario)
   elif antiguo >6:
      salario=(salario*20)/100+salario
      print("El sueldo del empleado es",salario)
else:
   print("El sueldo del empleado es",salario)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#9 Mostrar el número más grande (entre dos) ingresados por teclado. Si los dos números son iguales
#  mostrar el mensaje “Son iguales”.
print("Ejercicio 9")
numero1=float(input("Ingrese el primer número "))
numero2=float(input("Ingrese el segundo número "))
if numero1 > numero2:
   print(numero1,"es mayor a",numero2)
elif numero1==numero2:
   print("Son iguales") 
else:
   print(numero2,"es mayor a",numero1)
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#10 Hacer un programa que indique que si gasto por una compra $3000, pago en efectivo y obtengo un
#  descuento del 10% . Si gasto más de $3000 pero menos de $5000, pago con tarjeta de débito, sino pago con
#  tarjeta de crédito.
print("Ejercicio 10")
gasto=float(input("¿Cuanto gastó en la compra? "))
if gasto < 5000:
   if gasto <= 3000:
      gasto=gasto-(gasto*10)/100
      print("Pago con efectivo $",gasto)
   elif gasto < 5000:
      print("Pago con tarjeta de débito")
else:
   print("Pago con tarjeta de crédito") 
input("\033[1mPresione enter para continuar\033[0m")
os.system('cls')
#11 Se desea leer por teclado un número comprendido entre 0 y 10 (inclusive) y se desea visualizar si el número
#   es par o impar. (usar función random)
print("Ejercicio 11")
numRND=random.randint(0, 10)
print("El número es",numRND)
if numRND%2==0:
   print("El número es par")
else: 
   print("El número no es par")

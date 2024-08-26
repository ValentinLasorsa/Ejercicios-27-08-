import random
#1
""" 
categoria = input("Ingrese la categoría del socio ").upper()
socioVip=False
while categoria !="A" and categoria != "B" and categoria!="C":
   categoria = input("La categoría es incorrecta ").upper()
if categoria=="A":
   socioVip=True
antiguedad = int(input("Ingrese la antigüedad en el club en años "))
if antiguedad<10 or antiguedad>20 or categoria!="A":
   socioVip=False
else:
   print("Socio Vip")

#2
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

#3  
num=float(input("Ingrese número "))
if num%2==0:
   print("Es par")
else:
   print("No es par")

#4 
num1=int(input("Ingrese otro número "))
if num1%7==0:
   print("Es divisible por 7")
else:
   print("No es divisible por 7")
if num1>40:
   print("Es mayor a 40")
else:
   print("No es mayor a 40")

#5 Diseñar un programa que pida un número por teclado y luego imprima el número siguiente al ingresado.
numero=int(input("Ingrese otro número "))
numero=numero+1
print("El número siguiente es",numero)

#6
numAzar = random.randint(0, 200)
print("El número elegido es",numAzar)
numAzar=(numAzar*30)/100+numAzar
print("Y su potenciado es",numAzar)
"""
#7

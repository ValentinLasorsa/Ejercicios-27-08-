#1
"""
nombre=input("Ingrese su nombre ") 
apellido=input("Ingrese su apellido ")
nombreCompleto=nombre+""+apellido
print(str.upper(nombreCompleto))
print(str.lower(nombreCompleto))
print(str.title(nombre+""+apellido))

#2
nom=input("Ingrese su nombre ") 
print(str.upper(nom),"tiene",len(nom),"letras")

#3
palabra=input("Ingrese una palabra ")
caracter=input("Ingrese un caracter ")
while len(caracter)>1:
    caracter=input("Ingrese un caracter solo ")
palabra=palabra.upper()
caracter=caracter.upper()
print("El caracter aparece",palabra.count(caracter),"veces en la palabra")

#4
nombreYApellido=input("Ingrese nombre y apellido ")
nombreYApellido=nombreYApellido.lower()
print(str.title(nombreYApellido))
"""
#5
frase=input("Ingrese una palabra ")
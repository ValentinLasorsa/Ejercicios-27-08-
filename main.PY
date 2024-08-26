#1  Se ingresa por teclado la categoría de un socio del club deportivo y su antigüedad en años. Las
# categorías posibles son A, B y C. Luego se desea saber si el socio ingresado tiene categoría A o su
# antigüedad se encuentra entre los 10 y 20 años, en esos casos se pide mostrar un cartel que exprese
# lo siguiente: “Socio vip”.
categoria = input("Ingrese la categoría del socio ").upper()
while categoria !="A" and categoria != "B" and categoria!="C":
   categoria = input("La categoría es incorrecta ").upper()
antiguedad = int(input("Ingrese la antigüedad en el club en años "))
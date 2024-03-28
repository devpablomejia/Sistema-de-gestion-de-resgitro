import csv
import os 

def registro():
    nombre= str(input("ingrese su nombre "))
    numero_de_personas=int(input("numero de personas "))
    email= str(input("ingrese su email "))
    nacionalidad=str(input("de donde procede "))

    with open('registros.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([nombre, email, numero_de_personas, nacionalidad])
    print("Registro creado exitosamente.")



while True:
 print("BIENVENIDOS AL HOTEL LOS SANTOS ")
 registro()
 

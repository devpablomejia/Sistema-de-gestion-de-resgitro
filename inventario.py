import os 
def limpiar():
    os.system('cls')


    
print('BIENVENIDO AL POGRAMA DE INVENTARIO DE HABITACIONES'.center(60,'-'))
numero_de_habitacion= []
descripcion= []
precio= []


while True:
    print("""
    (1)añadir habitacion 
    (2)buscar habitacion
    (3)modificar habitacion
    (4)ver habitacion 
    (5)salir                
    """)

    respuesta= int(input('ingrese su opcion: '))
    if respuesta==1:
        ah= int(input('ingrese el numero de la habitacion: '))
        ad= str(input('ingrese la descripcion de la habitacion: '))
        ap= float(input('ingrese precio de la habitacion:: '))

        numero_de_habitacion.append(ah)
        descripcion.append(ad)
        precio.append(ap)
        limpiar()
        

    elif respuesta==2:
        buscador=int(input('ingrese numero de habitacion'))
        posicion =  numero_de_habitacion.index(buscador)  
        print('habitacion ', numero_de_habitacion [posicion])
        print('descripcion de la habitacion: ', descripcion[posicion])
        print('precio de la habitacion por noche: ', precio[posicion])
        

    elif respuesta==3:
         buscador=int(input('ingrese numero de habitacion')) 
         posicion =  numero_de_habitacion.index(buscador)      
         print('habitacion ', numero_de_habitacion [posicion])
         print('descripcion de la habitacion: ', descripcion[posicion])
         print('precio de la habitacion por noche: ', precio[posicion])
         ah= int(input('ingrese el numero de la habitacion: '))
         ad= str(input('ingrese la descripcion de la habitacion: '))
         ap= float(input('ingrese precio de la habitacion:: '))
         numero_de_habitacion[posicion]= ah
         descripcion[posicion]= ad
         precio[posicion]= ap
         

         

    elif respuesta==4:
        print('habitacion: ', numero_de_habitacion)
        print('descripcion: ', descripcion)
        print('precio: ', precio)
        

    else:
        print('ha salido del pograma') 
        limpiar()   
        break

import os 
print("BIENVENIDOS A SIREH".center(60,"*"))
n_habitacionpiso1=[ 101, 102, 103, 104, 105, 106, 107, 108, 109, 110]
n_habitacionpiso2=[ 201, 202, 203, 204, 205, 206, 207, 208, 209, 210]
n_habitacionpiso3=[ 301, 302, 303, 304, 305, 306, 307, 308, 309, 310]
n_habitacionpiso4=[ 401, 402, 403, 404, 405, 406, 407, 408, 409, 410]
n_habitacionpiso5=[ 501, 502, 503, 504, 505, 506, 507, 508, ]
n_habitacionpiso52=[509, 510]
descripcionA=['A: cuarto individual con un baño y salida a patio comunitario']
descripcionB=['B: cuarto doble con un baño con salida a balcon y beneficios en bufet ']
descripcionC=['C: cuarto king con dos camas dos baños y salida al mirador y beneficios en bufet']
descripcionD=['D: swit pricipal con tres camas dos baños y salida al mirador y uso del salon de eventos sin reserva beneficios de bufet incluidos']
preciosA=[70000]
preciosB=[120000]
preciosC=[180000]
preciosD=[210000]
ocupados=[]



while True:
    print("""
       (1)modificar inventarios de habitacion
       (2)ver habitaciones 
       (3)ver disponibilidad
       (4)realizar registro
       (5)ver registro
       (6)salir del pograma
       """)
    opcion=(int(input('ingrese su opcion de preferncia ')))
    if opcion==1:
        buscador=int(input('ingrese numero de piso '))
        if buscador==1:
            buscar1=int(input('ingrese numero de habitacion '))
            posicion1=n_habitacionpiso1.index(buscar1)
            print('habitacion ', n_habitacionpiso1 [posicion1])
            print('descripcion de la habitacion: ', descripcionA)
            print('precio de la habitacion por noche: ', preciosA)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah1= int(input('ingrese el numero de la habitacion: '))
            ad1= str(input('ingrese la descripcion de la habitacion: '))
            ap1= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso1[posicion1]= ah1
            descripcionA[0]= ad1
            preciosA[0]= ap1 
        if buscador==2:
            buscar2=int(input('ingrese numero de habitacion '))
            posicion2=n_habitacionpiso2.index(buscar2)
            print('habitacion ', n_habitacionpiso2 [posicion2])
            print('descripcion de la habitacion: ', descripcionB)
            print('precio de la habitacion por noche: ', preciosB)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah2= int(input('ingrese el numero de la habitacion: '))
            ad2= str(input('ingrese la descripcion de la habitacion: '))
            ap2= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso2[posicion2]= ah2
            descripcionB[0]= ad2
            preciosB[0]= ap2
        if buscador==3:
            buscar3=int(input('ingrese numero de habitacion '))
            posicion3=n_habitacionpiso3.index(buscar3)
            print('habitacion ', n_habitacionpiso3 [posicion3])
            print('descripcion de la habitacion: ', descripcionB)
            print('precio de la habitacion por noche: ', preciosB)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah3= int(input('ingrese el numero de la habitacion: '))
            ad3= str(input('ingrese la descripcion de la habitacion: '))
            ap3= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso3[posicion3]= ah3
            descripcionB[0]= ad3
            preciosC[0]= ap3   
        if buscador==4:
            buscar4=int(input('ingrese numero de habitacion '))
            posicion4=n_habitacionpiso4.index(buscar4)
            print('habitacion ', n_habitacionpiso4 [posicion4])
            print('descripcion de la habitacion: ', descripcionB)
            print('precio de la habitacion por noche: ', preciosB)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah4= int(input('ingrese el numero de la habitacion: '))
            ad4= str(input('ingrese la descripcion de la habitacion: '))
            ap4= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso4[posicion4]= ah4
            descripcionB[0]= ad4
            preciosB[0]= ap4      
        if buscador==5:
            buscar5=int(input('ingrese numero de habitacion '))
            posicion5=n_habitacionpiso5.index(buscar5)
            print('habitacion ', n_habitacionpiso5 [posicion5])
            print('descripcion de la habitacion: ', descripcionC)
            print('precio de la habitacion por noche: ', preciosC)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah5= int(input('ingrese el numero de la habitacion: '))
            ad5= str(input('ingrese la descripcion de la habitacion: '))
            ap5= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso5[posicion4]= ah5
            descripcionC[0]= ad5
            preciosC[0]= ap5  
        if buscador==5:
            buscar5=int(input('ingrese numero de habitacion '))
            posicion5=n_habitacionpiso5.index(buscar5)
            print('habitacion ', n_habitacionpiso5 [posicion5])
            print('descripcion de la habitacion: ', descripcionC)
            print('precio de la habitacion por noche: ', preciosC)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah5= int(input('ingrese el numero de la habitacion: '))
            ad5= str(input('ingrese la descripcion de la habitacion: '))
            ap5= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso5[posicion5]= ah5
            descripcionC[0]= ad5
            preciosC[0]= ap5      
        if buscador== 52:
            buscar52=int(input('ingrese numero de habitacion '))
            posicion52=n_habitacionpiso52.index(buscar52)
            print('habitacion ', n_habitacionpiso52 [posicion52])
            print('descripcion de la habitacion: ', descripcionD)
            print('precio de la habitacion por noche: ', preciosD)
            print('ingrese los nuevos valores'.center(60,"-"))
            ah52= int(input('ingrese el numero de la habitacion: '))
            ad52= str(input('ingrese la descripcion de la habitacion: '))
            ap52= float(input('ingrese precio de la habitacion:: '))
            n_habitacionpiso52[posicion52]= ah52
            descripcionD[0]= ad52
            preciosD[0]= ap52     
    elif opcion== 2:
          buscador2=int(input('ingrese numero de piso '))        
          if buscador2==1:
              print(n_habitacionpiso1)
              print(descripcionA)
              print(preciosA)
          if buscador2== 2:
              print(n_habitacionpiso2)
              print(descripcionB)
              print(preciosB)    
          if buscador2== 3:
              print(n_habitacionpiso3)
              print(descripcionB)
              print(preciosB) 
          if buscador2==4:
              print(n_habitacionpiso4)
              print(descripcionB)
              print(preciosB) 
          if buscador2==5:
              print(n_habitacionpiso5)
              print(descripcionC)
              print(preciosC)   
          if buscador2==52:
              print(n_habitacionpiso52)
              print(descripcionD)
              print(preciosD)            
    elif opcion==3:
        print("""
              (a)individual
              (b)doble
              (c)king
              (d)swit       """)
        buscador3=str(input('que tipo de habitacion desea'))
        if buscador3=="a":
            print(ocupados)
        if buscador3=="b":
            print(ocupados)
        if buscador3=="c":
            print(ocupados)
        if buscador3=="d":
            print(ocupados)    
    elif opcion==4:
         nombre=str(input('nombre de titular: '))
         numero_id=str(input('numero de documento: '))
         personas=str(input('numero de persona: '))
         contacto=str(input('numero de contacto:  '))
         habitacion=str(input('habitacion adquirida: '))
         numeror=str(input('numero de registro: '))

         ocupados.append(habitacion)

         with open('registrohuespedes.txt',mode='a') as file:
             file.writelines([nombre, numero_id, personas, contacto, habitacion, numeror])
             print('SU REGISTRO FUE EXITOSOS')

    elif opcion==5:
         with open('registrohuespedes.txt') as file_object:
             leer= file_object.readlines()
             for leer in leer:
                 print(leer.strip())   
    elif opcion==6:
        os.system('cls')
        print('USTED HA SALIDO DE SIREH'. center(60,"."))
        break

       

 
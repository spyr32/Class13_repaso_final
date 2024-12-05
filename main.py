#proyecto clase 13 final
#Autor Anthony Navarro Aguilar

import csv
import pandas as pd
import os

def menu():
    
    ventas =[]
    while True:

        print('\n---Menu principal--- ')
        print('1. Ingresar datos de ventas ')
        print('2. Guardar datos en un csv ')
        print('3. Analizar los datos guardados ')
        print('4. Salir del sistema ')
        opcion=input('Seleccione una opcion: ')
        
        if opcion == '1':
            print('\n ---Ingreso de ventas---')
            ingresar_datos(ventas)
        
        elif opcion == '2':
            
            print('\n --- Guardar datos de ventas---')
            
            guardar_csv(ventas)
        
        elif opcion == '3':
            
            print('\n --- Analizar datos de ventas---')
            
            analizar_ventas(ventas)
        
        elif opcion == '4':
            
            print('\n --- Saliendo del sistema---')
            
            break
        else:
            print('Opción no valida, vuelva a intentarlo')
                
            

def guardar_csv(ventas):
    
    if not ventas:
        
        print('No hay datos para guardar')
        return
                 
    with open('ventas.csv',mode = 'w') as file:
        
        guardado = csv.DictWriter(file,fieldnames=['producto','cantidad','precio'1,'fecha','cliente']) 
        
        guardado.writeheader()
        guardado.writerows(ventas)
    print('Datos guardados en el archivo.')    
             

def analizar_ventas(ventas):
    
    df = pd.read_csv('ventas.csv',encoding='latin-1')
    
    
    
    print(' \n ---Resumen de ventas---')
    #cual fue el total de ingresos generados
    df['Subtotal']=df['cantidad'] * df['precio']
    total = df['Subtotal'].sum()
    print(f'Total de ingresos $ {total:.2f}')
    
    #¿Cuál fue el total de ingresos generados?
    df['Subtotal'] = df['Cantidad'] * df['Precio']
    Total = df['Subtotal'].sum()
    print(f'Total de ingresos ₡{Total:.2f}')


    #¿Cuál fue el producto más vendido?
    producto_mas_vendido = df.groupby('Producto')['Cantidad'].sum().idxmax()
    #cantidad_vendida =  df.groupby('Producto')['Cantidad'].sum()
    print(f'El producto mas vendido es {producto_mas_vendido} con estas unidades ')
    
    print(producto_mas_vendido)           

def ingresar_datos(ventas):

   
   while True:
        #Entrada de datos
   
    producto=input('Ingrese el nombre del producto: ')
    cantidad=int(input('Ingrese la cantidad vendida: '))
    precio=float(input('Ingrese precio x unidad: '))
    fecha=input('Ingrese la fecha de la venta (yyyy-mm-dd)')
    cliente=input('Ingrese el nombre del cliente: ')
    
    if cantidad <= 0:
        
        print('La cantidad debe ser mayor a 0. Intentelo de nuevo')
        
    if precio <= 0:
        
        print('Precio no valido, intentelo de nuevo') 
        
    venta ={
        'producto':producto,
        'cantidad':cantidad,
        'precio':precio,
        'fecha':fecha,
        'cliente':cliente
        
    }  
    
    ventas.append(venta)
    
    continuar = input('Desea ingresar otra venta? (s/n)').lower()
    
    if continuar == 'n':
        break
        
    
    
                
        
#Validar la ejecucion del archivo principal
if __name__ == '__main__':
    print("Bienvenido al sistema de gestion de ventas")
    menu()

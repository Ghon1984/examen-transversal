import random

sueldos=[]
from random import randint
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
nombres=trabajadores
def generar_sueldos():
    for nombre in trabajadores:
        print(f"el nombre es  : {nombre}  y    su    sueldo es :{str(randint(100000,2500000)).ljust(10)} ")
        sueldos.append({randint(100000,2500000)})        
opcion=0   
def registro():
    for sueldo in sueldos:
        if  sueldo["sueldo"]<=800000:
            print(f"su sueldo es {sueldo}")
        elif sueldo["sueldo"]<=800000:    
             print(f"su sueldo es {sueldo}")
        else:
             print(f"su sueldo es {sueldo}")  
def imprimir():
        prueba=open("prueba.csv","w")       
        prueba.write(f"los datos son {trabajadores} y el sueldo es {randint}") 
        
        prueba.close()    
              
def menu():             
    print("1. Asignar sueldos aleatorios")
    print("2. Clasificar sueldos")
    print("3. Ver estadísticas")
    print("4. Reporte de sueldos")
    print("5. Salir del programa")
while opcion!=5:
       menu()
       opcion=int(input("eliga una opcion:")) 
       if opcion==1:
          generar_sueldos() 
       elif opcion==2:
            print(sueldos)
       elif opcion==3:
            imprimir()
       elif opcion==5:
            print("saliendo del programa")     
                
         
         
      
            
                
            
       
           
      
      
          
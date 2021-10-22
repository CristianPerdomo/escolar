import time
import re
import os
#______Edades____#
'''while True:	
    usuario = int(input("La edad NO debe ser negativa: "))
    if usuario < 0:
    		print("Edad invalida")
    else:
        if usuario >= 18:
            print("Eres mayor de edad")
        else:
            if usuario > 18:
                print("Eres un adulto")
            else:
                if usuario >= 65:
                    print("Eres adulto mayor")'''

"""while True:
    usuario=int(input("Taba de multiplicar: "))
    for i in range (16):
        tabla = i * usuario
        print(i,"X",usuario," = ",tabla)"""
'''while True:
    n1=float(input("Dijite nota 1: "))
    n2=float(input("Dijite nota 2: "))
    n3=float(input("Dijite nota 3: "))
    def Por_nota(not1,not2,not3):
        d=o,2
        f=0,3
        t=0,5
        c1=not1*d                
        c2=not2*f    
        c3=not3*t
        resultado=c1+c2+c3
        print(resultado)
    calificacion=Por_nota(n1,n2,n3)'''
    
    #descuento por venta
    
'''''hile True:
    while True:
        usuario=int(input("Ingrese valor: "))
        if usuario >= 1000000:
            descuento3 = usuario*10/100
            print("\n Precio sin descuento: ",usuario,"\n","Precio con descuento: ",descuento3,"$")
        elif usuario >= 500000:
            if usuario < 1000000:
                descuento5=usuario*5/100
                print("\n Precio sin descuento: ",usuario,"\n","Precio con descuento: ",descuento5,"$")
        elif usuario >= 100000:
            if usuario < 500000:
                descuento5=usuario*3/100
                print("\n Precio sin descuento: ",usuario,"\n","Precio con descuento: ",descuento5,"$")
        elif usuario < 100000:
            print("\n No cumples con el monto total para descuento\n","Precio a pagar: ",usuario,"$")
        else:
            if usuario < 100000:
                print("\n no entiendo por favor reintentar\n")    '''
#REALICE UN SOFTWARE que lea 3 numeros y diga cual es el mayor
while True:
    def continuar():
        salir=str(input("¿Desea salir del programa? / oprima enter para continuar "))
        if salir == "si":
            cerrando="cerrando programa "
            for carga in range(10):
                mostrar=print(cerrando)
                tiempo_de_carga2=time.sleep(0.5)
                cerrando=cerrando+"."
                borrar=os.system("cls")
            quit()
        else:
            pass                
    for i in range(3):
        num1=int(input("Dijite numero: "))
        num2=int(input("Dijite numero: "))
        num3=int(input("Dijite numero: "))
        if num1 > num2:
            if num1 > num3:
                if num3 > num2:
                    print("\n",num2,"\n",num3,"\n",num1,"\n")
                else:
                    print("\n",num3,"\n",num2,"\n",num1,"\n")
            else:
                print("\n",num2,"\n",num1,"\n",num3,"\n")
        else:
            if num2 > num3:
                if num2 > num1:
                    print("\n",num3,"\n",num1,"\n",num2,"\n")
                else:
                    print("\n",num1,"\n",num3,"\n",num2,"\n")
            else:
                print("\n",num1,"\n",num2,"\n",num3,"\n")
        continuar()
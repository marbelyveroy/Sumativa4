print('\t\t ESCUELA POLITECNCA NACIONAL')
print('INTEGRANTES:')
print('\t\t Edison Osorio')
print('\t\t Micha Cardenas')
print("\t\t Stalin Maza")
import sys
import math
                    #FUNCIONES DE LAS FIGURAS
#crear txt triangulo, cuadrado
def crear_E():
    archT=open('TRIANGULO.txt','w')
    archC=open('CUADRADO.txt','w')
    archO=open('OCTAGONO.txt','w')
    archO.close()
    archT.close()
    archC.close()
    
def triangulo():
    archT=open('TRIANGULO.txt','a')
    print('\tTRIANGULO')
    lado=int(input('Ingrese la longitud del lado (base):\n'))
    altura=int(input('Ingrese la altura:\n'))
    area=(lado*altura)/2
    perimetro=lado*3
    print('El area del triangulo es: ',area)
    print('El perímetro del triángulo es: ',perimetro)
    #grabar los resultados en el txt
    archT.write(str(area))
    archT.write('\n')
    archT.write(str(perimetro))
    archT.close()
    

def cuadrado():
    archC=open('CUADRADO.txt','a')
    print('\tCUADRADO')
    lado=int(input('Ingrese la longitud del lado: \n'))
    area=lado*lado
    perimetro=lado*4 
    print('El area del cuadrado es: ',area)
    print('El perímetro del cuadrado es: ',perimetro)
    #grabar los resultaos en txt
    archC.write(str(area))
    archC.write('\n')
    archC.write(str(perimetro))
    archC.close()
    

def pentagonoR():
    print("\tPENTAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))
    temp = perimetroF(5,lado,"Pentagono")
    areaF(temp,apotemaF(lado,5),"Pentagono")#calcula el area
    creartxt("PENTAGONO_REGULAR")
    grabartxt(temp,areaF,"PENTAGONO_REGULAR")
    
def hexagonoR():
    print("\tHEXAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))    
    temp = perimetroF(6,lado,"Hexagono")
    areaF(temp,apotemaF(lado,6),"Hexagono")#calcula el area
    creartxt("hexagono_regular")
    grabartxt(temp,areaF,"hexagono_regular")

def heptagonoR():
    print("\tHEPTAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))   
    temp = perimetroF(7,lado,"Heptagono")
    areaF(temp,apotemaF(lado,7),"Heptagono")#calcula el area
    #crear el txt de la figura
    creartxt("HEPTAGONO")
    #guardamos en el txt 
    grabartxt(temp,areaF,"HEPTAGONO")
    

def octagono():
    archO=open('OCTAGONO.txt','a')
    print("\t OCTAGONO REGULAR")
#se puede calcular mediante el ángulo centra lo cual no sirve para sacar el apotema
    angulo_central=360/8
#ingresamos el lado 
    lado=int(input ("Ingrese el lado del octagono regular"))
#calculo del perimetro n *l
    perimetro=8*lado
    apotem=lado/(2*math.tan(angulo_central/2))
    area=lado= 4*lado*apotem
    print("el perimetro del octagono regular es",perimetro)
    print (" el apotema es ",apotem)
    print("el area es ",area)
    archO.write(str(area))
    archO.write('\n')
    archO.write(str(perimetro))
    archO.close()
   

def eneagono():
    lado=int(input ("Ingrese el lado del eneagono regular"))
    perimetro=lado*9
#Formula sacar el area de una figura de 9 lados
    area=9*(lado*lado)/(4 * math.tan(180/2))
    print("el perimetro del eneagono regular es",perimetro)
    print("el area es ",area)
     #crear el txt de la figura
    creartxt("ENEAGONO")
    #guardamos en el txt 
    grabartxt(perimetro,area,"ENEAGONO")
    
    
def decagono ():
    lado=int(input ("Ingrese el lado del decagono regular"))
    perimetro=lado*10
#Formula sacar el area del decagono
    area=10*(lado*lado)/(4 * math.tan(180/10))
    print("el perimetro del decagonno regular es",perimetro)
    print("el area es ",area)
    #crear el txt de la figura
    creartxt("DECAGONO")
    #guardamos en el txt 
    grabartxt(perimetro,area,"DECAGONO")
    
    
                        #OPERACIONES MATEMATICAS   
def perimetroF(NumL,LongL,nombre):
    per = NumL * LongL #calcula el perimetro
    print("El perímetro del ",nombre," es: ",per)
    return per

def areaF(per,apotema,nombre):    
    areaT = (per*apotema)/2  #calcula el area
    print("El area del ",nombre," es: ",areaT)
    return areaT

def apotemaF(lado,n):
    conversion = math.radians(360/n)
    tangente = math.tan(conversion/2)
    apot = lado/(2*tangente)  
    return apot
#FUNCIONES PARA CREAR Y GRABAR TXTS
def creartxt(nombre):
    name = nombre + ".txt"
    archi = open(name,"w")
    archi.close()

def grabartxt(perimetro,area,nombre):
    name = nombre + ".txt"
    print(perimetro)
    print(area)
    a = str(perimetro)
    b = str(area)
    archi=open(name,"a")
    archi.write("El perimetro es: " + a +"\n")
    archi.write("El area es: " + b + "\n")
    archi.close()



    
    
                        #MENU Y SWITCH    
def switch(NumLados):    
    if NumLados=='3':
        triangulo()
        repetir()
    elif NumLados=='4':
        cuadrado()
        repetir()
    elif NumLados == '5':   #aqui realizamos las opciones del switch de acuerdo a lo que escoga
        pentagonoR()        #a lo que escoga el usuario.
        repetir()
    elif NumLados == '6':
        hexagonoR()
        repetir()
    elif NumLados == '7':
        heptagonoR()
        repetir()
    elif NumLados == '8':
        octagono()
        repetir()
    elif NumLados == '9' :
        eneagono()
        repetir()
    elif NumLados =='10':
        decagono()
        repetir()
    else:
        print("¡¡ERROR!!..NUMERO DE LADOS DEBE ESTAR EN RANGO DE 3 A 10")
        menu()
        
def menu():
    NumLados =input('INGRESE EL # DE LADOS\n')   
    switch(NumLados) #Este es el que recibe el numero de lados    
            
def repetir():
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        menu()   #aqui damos la opcion al usuario de si desea continuar en el programa
    print ("Programa Terminado")
    sys.exit()
    
def main():
    #llamar a la funcion crear txt
    crear_E()
    #creartxt("juanito")
    menu()    #llamamos a la funcion del menu

main()

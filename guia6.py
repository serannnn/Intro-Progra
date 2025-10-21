def suma2(x: int, y: int) -> int:
    res: int = x + y
    return print("El resultado es",res)

# Ej 1.1
#Ejercicio 1. Definir las siguientes funciones y procedimientos
#1. problema imprimir hola mundo () {
#requiere: { True }
#asegura: { imprime ’Hola Mundo’por consola}
#}
from math import sqrt, pi , ceil , floor 

def imprimir_hola_mundo():
    print("hola"," ","mundo!")

'''
. imprimir_un_verso(): que imprima un verso de una canción que vos elijas, respetando los saltos de línea mediante
el caracter. '''

def imprimir_un_verso():
    print("Disparo","proyectiles","en","el","rap","de","capablanca")
    print("yo","hago","que","asimiles","y","asi","mires","la","verdad","pa"".")


def raizDeDos():
    res = round(sqrt(2) , 4)
    return print("El resultado es", res)
def factorial_2 (x: int) -> int :
    x=2 
    res: int = x * (x-1)
    return print("Nuestro resultado es", res)

def circunsferencia():
    x= 2 * pi # formula de circunsferencia de radio 1. (2*pi*r)
    res = round(x , 4) # redondeo de cifras significativas (4 en total)
    return print("La circunsferencia de un circulo es", res)

def imprimir_saludo(nombre: str):
    print("Hola",nombre,"como estas?")
    print("Un placer tenerte aqui.")

def raizCuadrada(x: int) -> float:
    x = sqrt(x) # x sera nuestra raiz cuadrada
    res: float = round(x , 5)  # nos devuelve un aproximado en 5 cifras significativas.
    return print("La raiz cuadrada es", res) 

def f_a_c(x: int) -> float :
    x = ((x-32) * 5) / 9
    res: float = round(x , 2)
    return print("Nuestra temperatura en Cº es", res)

def imprimir_dos_veces(estribillo : str):
    estribillo : str = ("Disparo","proyectiles","en","el","rap","de","capablanca")
    res = 2 * estribillo 
    return res

def es_multiplo(n: int , m: int) -> bool :
    res: bool = n % m == 0 
    return res

def es_par(n: int)-> bool:
    res: bool = es_multiplo(n, 2)
    return res
def es_impar(n: int) -> bool:
    res: bool = not (es_multiplo(n, 2))
    return res

# punto 7 cantidad_de_pizzas(comensales, min_cant_de_porciones) 

def cdp(comensales: int, mcdp: float) -> int:
    total_porciones: int = comensales * mcdp 
    res: int = ceil(total_porciones/8)
    return res

# ejercicio 3. 

def alguno_es_0(n: float, m: float) -> bool:
    res: bool = n == 0 or m == 0 
    return res 

def ambos_son_0(n: float , m: float) -> bool:
    res: bool = n == 0 and m == 0
    return res

def es_nombre_largo(nombre: str) -> bool: 
    res: bool = len(nombre) > 8   
    return res

def es_bisiesto(año: int) -> bool:
    res: int = es_multiplo(año, 400) or es_multiplo(año, 4) and (not es_multiplo(año, 100))
    return res 

# el peso de un pino se estima a partir de la altura
# es decir, 3kg por cada centimetro, hasta 3 metros.
# y luego 2kg por cada cm arriba de los 3 metros.
# 2 metros pesan 600kg pues 200*3 es 600kg.
# 5 metros pesan 1300 kg, pues 300*3 y 200*2 (900+400) = 1300...


def operacion_peso(altura: int) -> int:
    cm = altura * 100 # pasaje a cm
    p1 = min(cm, 300) * 3 # si altura es 3, cm sera 300 pues tomara 300, si la altura es 2 tomara 200, pues 2m * 100 es 200.
    p2 = max(cm - 300, 0) * 2 # si la altura es 500 cm, restamos 300 cm (tomamos el max) y luego multiplicamos * 2 (kg)
    p3 = p1 + p2  # suma de ambos, si el primero es menor o igual a 3 kg, y el segundo es mayor a 3 (estrictamente.) del segundo restamos 300 cm del primero y multiplicamos por 2kg/cm   
    return p3 # devolvemos la suma total.

def es_peso_util(peso: int) -> bool:
    utilidad: bool = peso >= 400 and peso <= 1000 # chequeamos si el peso esta entre 400kg y 1000kg. si es así true, si no es así false.
    return utilidad

def sirve_pino(altura: int) -> bool:
    peso = operacion_peso(altura) # primero nos fijamos en el peso del pino
    p1 = es_peso_util(peso)  # luego nos fijamos si es peso util, es decir si esta entre 400kg y 1000kg.
    return p1
    

def sirve_pino2(altura: int) -> bool:
    res: bool = es_peso_util(operacion_peso(altura)) # hacemos una composicion de funciones, decidimos si es peso util, aplicando como argumento el peso del pino directamente.
    return res # devolvemos la funcion.

def devolver_el_doble_si_es_par(n: int) -> int:
    n: int 
    if es_par(n): # si es par nos devuelve el par duplicado.
        n = 2*n
    else:
        n = n     # si es impar nos devuelve el mismo n.        
    return n 

def devolver_par_sino_siguiente(n: int) -> int:
    n: int 
    if es_par(n):
        n = n 
    else:
        n = n+1 
    return n 

def devolver_par_sino_siguiente2(n: int) -> int:
    n: int 
    if n % 2 == 0 :
        n = n
    else:
        n = n+1
    return n 

def devolver_par_sino_siguiente3(n: int) -> int:
    n: int 
    if es_par(n):
        n = n 
    elif es_impar(n):
        n = n+1
    else:
        n = n+1
    return n

def devolver_par_sino_siguiente4(n: int) -> int:
    n: int 
    if n % 2 == 0:
        n = n 
    elif n % 2 != 0:
        n = n+1
    else:
        n = n+1
    return n

def devolver_m3_m9(n: int) -> int:
    n: int
    if es_multiplo(n, 3):
        n = 2 * n 
    elif es_multiplo(n,9):
        n = 3 * n 
    else:
        n = n 
    return n 

def lindo_nombre(nombre: str) -> str:
    nombre: str
    if len(nombre)>=5:
        print("Tu nombre tiene muchas letras!")
    else:
        print("Tu nombre tiene menos de 5 caracteres")
    return nombre

def elRango(n: int) -> str:
    n: int
    if n<5:
        print("Menor a 5")
    elif n>=10 and n<=20:
        print("El número esta entre 10 y 20")
    else:
        print("Tu numero no esta en el rango o")
        print("El número es mayor a 20 xD")        
    return n

def mujer_jubilada(edad: int) -> bool:
    res: bool = edad >= 60 
    return res
def hombre_jubilado(edad: int) -> bool:
    res: bool = edad >= 65
    return res
def menores_edad(edad: int) -> bool:
    res: bool = edad < 18 
    return res

def jubilacion_o_joven(edad: int, sexo: str) -> str:
    sexo: str
    
    if sexo == "Niños" and menores_edad(edad):
        print("Se van de vacaciones!!")
    elif sexo == "Hombres" and hombre_jubilado(edad):
        print("Se van de vacaciones!")
    elif sexo == "Mujeres" and mujer_jubilada(edad):
        print("Se van de vacaciones")        
    else:
        print("Toca laburar che..")
    return sexo 

def uno_al_diez(n: int) -> int:
     
    while 1<=n<=10:
        print(n)
        n += 1
    print("Terminamos de contar")

def pares_hasta_40(n: int) -> int:
    while es_par(n) and 10<=n<=40:        
        print(n)
        n += 2
    print("Se acabo")

def eco(n: str) -> str:
    n: str = ("Eco")
    contador = 0
    num_repetir = 10

    while contador < num_repetir:
        print(n)
        contador += 1 

def cuenta_regresiva(n: int)-> int:
    contador: int = n 
    final: int = 0 
    while contador > final:
        print(contador)
        contador -= 1 
    print("Despega wachin")

def viaje_en_el_tiempo(año_partida: int , año_llegada: int):
    while año_partida > año_llegada:
        año_partida -= 1
        print(año_partida)
        print("Viajó un año al pasado, estamos en el año:", año_partida)

def viaje_en_el_tiempo2(partida: int):
    salto = 20 
    llegada = -384
    while partida > llegada:
        if partida - salto < llegada:
            salto = partida - llegada # ajusta el salto para no pasarse
        partida -= salto 
        print(partida, "años")
        print("cada vez mas cerca de 384 a.C =).") # revisar ejercicio; 

def ejecucion_simbolica():
    x = 5
    y = 7
    x = x + y 
    return x         

def ejecucion_simbolica2():
    x = 5
    y = 7
    z = x + y 
    y = z * 2 
    return z 


def ejecucion_simbolica3():
    x = 5
    y = 7
    x = "hora" 
    y = x * 2
    return x

def ejecucion_simbolica4():
    x = False 
    res = not(x)
    return res 

def ejecucion_simbolica5():
    x = True
    y = False 
    res = x and y 
    x = res and x 
    return x 

# ejercicio 7 jijo

#a)
def f_1_10(n: int) -> int:
    for n in range(n,11, 1):
        print(n)
#b)
def p_10_40(n: int) -> int:
    for n in range(10, 42, 2):
       print(n)


def eco_diez_veces(n: str):
    for n in range (10):
        print("eco")

def  c_regresiva(n: int):
    for n in range(n, -1, -1): # hacemos la cuenta regresiva
        print(n)
    if n == 0: # cuando el contador llega a 0 nos vamos a chinardaa!
        print("Despegamos gamuza!")     

def viaje_in_time(partida: int, llegada: int):
    if llegada < partida:
        for año in range(partida -1, llegada -1, -1):
            print("Viajo un año al pasado, estamos en el año", año)




        

    


        

    
    

  
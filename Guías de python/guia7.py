## arrancamos con la guia 7 de pyton, listas, arreglos, pila y cola.
from array import * # importamos el modulo array.
a: array = array('i' , [1,2,3]) # array esta definido como (tipo de dato(expresado en unicode), secuencia del tipo de dato) .

'''
No esta mal decir que:
a[i] -> nos devuelve la posicion x de la secuencia, teniendo en cuenta que el indice arranca en 0. 
a[i] = x -> nos devuelve un x diferente, modificando la posicion x en el array.
a.append(x) -> añade a x como nuevo elemento de a. un ej: a.append(4) de [1,2,3] -> [1,2,3,4] (funciona en listas.) # agrega un elemento a la ultima posicion
a.remove(x) -> elimina el primer elemento de a, que coincida exactamente con x. un ejemplo a.remove(1) -> [1,2,3] -> [2,3] # nos quita el elemento x.
a.index(x) -> obtiene la posicion donde aparece por primera vez el elemento x. ejemplo: a.index(3) -> [1,2,3] -> 2  # recordar que el indice arranca en 0.
a.count(x) -> devuelve la cantidad de apariciones del elemento x. ejemplo: a.count(1) ->  [1,2,3,1,2] -> 2 (cuenta la cantidad de veces que aparece x en la secuencia)
a.insert(p,x) -> inserta el elemento delante de la posicion p. 
'''
'''
Cuando hablamos de listas, podemos decir que son relativamente parecida a los arrays. Peeeero, con el hecho de que los arrays son mas eficientes en terminos de memoria, en cambio las
listas no, y otra cosa muy importante es que los arrays solamente estan sujetos a un unico tipo de dato, en cambio las listas no. Para entrar en calor daremos unos ejemplos:
variableLista = [] -> es una lista vacia.
variableLista2 = list() -> tambien lo es, solamente que tiene distinta notacion
otraVariable = [1, "hola", True, 5]
anotherOne = list([1, "hola", False, 3])
'''
# un ejemplo

x = 100 # variable global
def funcion_rara():
    x = 100 / 2 # variable local -> es decir modificamos la global, unicamente de manera local.
    res = x + x 
    return print("el numero es", res * 2)


def pertenece(s:list, e: int) -> bool:
    for elemento in s:
        if elemento == e:
            return True
    else:
        return False    

def pertenece2(s: list, e: int) -> bool:
    if s.count(e) == 0: # si la cantidad de apariciones de e es 0, no esta en la lista.
        return False
    else:
        return True 

def pertenece3(s: list, e: int) -> bool:
    i = 0 
    while i<len(s): # el indice debe ser menor que la longitud de s
        if s[i] == e: 
            return True
        i += 1
    return False 

def divide_a_todos(s: list, e: int) -> bool:
    for elemento in s:
        if elemento % e == 0:
            return True
        else:
            return False
        
def suma_total(s: list[int]) -> int:
    total: int = 0  # contador, donde almacenare la suma.
    for x in s: 
        if len(s) > 0: # si la cantidad de elementos es mayor que 0.
            total += x # le agrego al total la suma de cada elemento.
    return total # devuelvo la cantidad total de elementos sumados.

'''
Debo hallar el maximo de una lista, es decir si tengo [1,2,3,4], la funcion me deberia de devolver 4 en este caso.
si tengo la lista [1,4,2,9,5] en este caso nos deberia devolver el 9.
nos requiere que la longitud de la lista sea > 0lemento: int = 0
debo tomar un elemento de la lista s, y comparar con los demas elementos.
si es mayor lo almaceno, si es menor sigo con el otro. 
'''
def maximo(s: list[int]) -> int:
    maximo = s[0]  # lista no vacia
    for x in s: # recorro toda la lista buscando el x mas grande.
        if x > maximo: # cualquier elemento mayor a "maximo"
            maximo = x # le agregamos ese valor a maximo
    return maximo   # devolvemos ese valor

def minimo(s: list[int]) -> int:
    minimo = s[0] # lista no vacia.
    for x in s: # recorro toda la lista buscando el x mas chico
     if x < minimo: # si x es menor al minimo.
         minimo = x  # a minimo le asigno el valor mas chico, osea "x"
    return minimo # retorno el valor mas chico almacenado en minimo.

'''
-> para todo i entero, si 0 <= i < longitud(s)-1  ---> s[i] < s[i+1] // decimos que el indice puede arrancar en 0.
ejemplo; i = 0 y s una lista [1,2,3]. 
0 = 0 < 3-1 , s[0] = 1 < s[1] = 2 -> s[i] == num 
0 < 2  ---> 1 < 2 . (i= indice) -> True, 
[1,3,1]
indice = 1
0 = 0 < 2 , s[1] = 3 , s[2] = 1 3 < 1 ? No. 
'''
#1.6

def ordenados(lista: list[int]) -> bool:
    
    for indice in range(len(lista)-1): # recorremos por indice cada elemento de la lista.
       if lista[indice] >= lista[indice + 1]:
           return False
    return True 

# 1.7


def pos_maximo(lista: list[int]) -> int:
    if len(lista) == 0: # cuando la longitud de la lista es 0 devuelvo -1
        res = -1
        return res
    elif len(lista) != 0: 
        for indice in range(len(lista)): # recorro la lista por indice, y donde es el e
            if maximo(lista) == lista[indice]:
                return indice
            
# 1.8
            
def pos_minimo(lista: list[int]) -> int:
    if len(lista) == 0:
        res = -1
        return res
    for indice in range(len(lista)):
        if minimo(lista) == lista[indice]:
            return indice  

# 1.9

# ejemplo de seq(seq(char))
[["hola"],["como"],["estas"],["?"]]

def palabra_linda(p: str) -> bool:
    if len(p) <= 7:
        return True
    else:
        return False
    


def long_mayor_a_7(lista: list[list[str]]) -> bool:

    for sublista in lista: # para cada sub secuencia de la lista
        for palabra in sublista: # recorro cada palabra en la sub secuencia
            if not palabra_linda(palabra): # analizo si la longitud de la palabra es mayor que 7
                return False # retornamos False
    return True # de lo contrario devolveremos True




# lo que me interesa de la funcion es palindroma es comparar letra por letra de cada palabra sin importar que palabra sea, es decir
# es como ir comparando por indices no? si el primer indice es igual al ultimo indice, el segundo al anteultimo y asi, pues es palindroma.

# nos estan pidiendo analizar algo del tipo ["hola","como","estas"]
# y analizar por cada cadena de texto si es un palindromo la palabra o no.

def palabra_rever(p: str) -> str:
    palabra: str = ""
    for indice in range(len(p)-1, -1, -1):
        palabra += p[indice]
    return palabra


def es_palindromo(lista: list[str]) -> bool:
     for palabra in lista: # analizo las palabras en la lista
         if palabra != palabra_rever(palabra): # llamo a la funcion palabra_rever (que me devuelve una palabra al reves)
             return False
     return True 

def iguales_consecutivos(lista: list[int]) -> bool:
    for i in range(len(lista)-1): # i = indice.
        if lista[i] == lista[i+1] == lista[i+2]: # me fijo si nuestro numero en esa posicion i es igual al siguiente, y al siguiente, es decir si son consecutivos.
            return True # si lo son (no me importa en que posicion) devolvemos que la funcion es True
    return False # en caso contrario decimos que la funcion no se cumple, por lo tanto devolvemos False.

# Recorrer una palabra en formato string y devolver True si ´esta tiene al menos 3 vocales distintas 
# y False en caso contrario.

def es_vocal(palabra: str) -> bool:
    if palabra == "a" or palabra == "e" or palabra == "e" or palabra == "i" or palabra == "o" or palabra == "u":
        return True
    else:
        return False

def vocales_distintas(lista: list[str]) -> bool:
    for palabras in lista:
        for i in range(len(palabras)):
            if es_vocal(palabras[i]): # señalo si en cada letra es vocal, seguimos iterando.
               for j in range(len(palabras)): # iteracion para el el indice j
                  if  es_vocal(palabras[j]):  # si tiene vocales la palabra en el indice j seguimos iterando..
                     for k in range(len(palabras)): # iteracion para el indice k
                         if  es_vocal(palabras[k]): # si hay alguna vocal en el indice k 
                            if palabras[i] != palabras[j] and palabras[i] != palabras[k] and palabras[j] != palabras[k]:
                                return True
        return False

if __name__ == "__main__":
    print(vocales_distintas(["ituzaingo"]))


def pos_secuencia_ordenada_mas_larga(s: list[int]) -> int:
    inicio_max = 0
    longitud_max = 1
    inicio_actual = 0
    longitud_inicial = 1

    for i in range(1, len(s)):
        if s[i] >= s[i - 1]: # si la subsecuencia es creciente
            longitud_inicial += 1 # entonces la longitud crece.
        else:
            if longitud_inicial > longitud_max:
                longitud_max = longitud_inicial
                inicio_max = inicio_actual
            inicio_actual = i
            longitud_inicial = 1
    if longitud_inicial > longitud_max:
        inicio_max = inicio_actual
    return inicio_max

def es_par(num: int) -> bool:
    if num % 2 != 0:
        return False
    return True
    
def cantidad_digitos_impares(s: list[int]) -> int:
    contador_impares = 0
    for numeros in range(len(s)): # recorro los numeros por indice.
        if not es_par(s[numeros]): # chequeo si no es impar
            contador_impares += 1 # hago el conteo de impares
    return contador_impares # devuelvo el contador.

def ceros_en_pos_pares(secuencia: list[int]):
    for x in range(len(secuencia)):
        if es_par(secuencia[x]):
            secuencia[x] = 0 # modificamos el valor de la secuencia en ese indice. (si es par)
    return secuencia # devuelvo la secuencia, si hay un par lo reemplaza por 0.

def cero_en_pos_pares2(secuencia: list[int]) -> list[int]:
    nueva_secuencia: list[int] = []
    for numeros in range(len(secuencia)):
        if es_par(numeros):
            numeros = 0
            nueva_secuencia.append(0)
        elif not es_par(numeros):
            nueva_secuencia.append(secuencia[numeros])
    return nueva_secuencia

def es_vocal2(char: chr) -> bool:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u": 
        return True
    else:
        return False

def sin_vocales(secuencia: list[chr]) -> list[chr]:
    sec_sin_vocales: list[chr] = []
    for char in range(len(secuencia)):
        if not es_vocal2(secuencia[char]):
            sec_sin_vocales.append(secuencia[char])
    return sec_sin_vocales

def reemplaza_vocales(secuencia: list[chr]) -> list[chr]:
    reemplazo_vocales: list[chr] = []
    for letras in range(len(secuencia)):
        if es_vocal2(secuencia[letras]):
            reemplazo_vocales.append(" ")
        else:
            reemplazo_vocales.append(secuencia[letras])
    return reemplazo_vocales

def da_vuelta_str(secuencia: list[chr]) -> list[chr]:
    reversa_mami: list[chr] = []
    for l in range(len(secuencia)-1, -1, -1): # notamos que range (inicio, freno, paso)
        reversa_mami.append(secuencia[l]) # como iremos desde el ultimo al primero, en la nueva lista agregamos el indice recorrido de forma invertida.
    return reversa_mami # devolvemos nuestra nueva secuencia. idem para hacer palabras invertidas.

## si el elemento se repite solo lo agregamos 1 vez a la nueva lista.


def eliminar_repetidos(secuencia: list[chr]) -> list[chr]:
    lista_sin_repetidos: list[chr] = []
    for char in range(len(secuencia)): 
        if not pertenece(lista_sin_repetidos, secuencia[char]): # si no pertenece nuestro char a la secuencia, lo agregamos.
            lista_sin_repetidos.append(secuencia[char]) # agregamos el char a la nueva secuencia.
        else:
            lista_sin_repetidos.remove(secuencia[char]) # de lo contrario, lo quitamos.
    return lista_sin_repetidos # retornamos nuestra funcion sin su repetido.

def suma_total2(s: list[int]) -> int:
    totalidad: int = 0
    for x in s:
        if len(s)>0:
            totalidad += x
    return totalidad
# ejercicio 3

def resultado_materia(notas: list[int]) -> int: 
    for i in range(len(notas)):
        if notas[i] >= 4 and notas[i] <= 10:
            if  (suma_total2(notas) / len(notas)) >= 7:
                return 1
        if notas[i] >= 4 and notas[i] <= 10:
            if  4 <= (suma_total2(notas) / len(notas)) <= 7:
                return 2
    return 3

# ejercicio 4
# tengamos en cuenta que la tupla va a tener dos valores, uno que sera;
# Ingresos, y otro retiro, y en el otro la guita.
# es decir ("I", 2000) -> ("R", 1000) = 1000.
def saldoActual(movimientos: list[tuple[str, int]]) -> int:
    saldo: int = 0
    for h in range(len(movimientos)):
        if movimientos[h][0] == "I" and movimientos[h][1] >0:
            saldo += movimientos[h][1]
        elif movimientos[h][0] == "R" and movimientos [h][1]>0:
            saldo -= movimientos[h][1]
    return saldo

# ej 5 . MATRICES

def pertenece_a_c_uno_v1(s: list[list[int]], e: int) -> list[bool]:
    for sec in range(len(s)):
        if not pertenece(s[sec], e):
            return False
    return True






    









            

 




          

        
        

           


    


        














            
            
            











        
        

                  




   
                            

             


        
        


         
             
     

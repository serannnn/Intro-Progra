from queue import LifoQueue as Pila
from queue import Queue as Cola


import random

def generar_nros_al_azar(desde, hasta, cantidad) -> Pila[int]:
    res: Pila[int] = Pila()
    for _ in range(0, cantidad):
        res.put(random.randint(desde, hasta))
        res.qsize() == cantidad
    return print(list(res.queue))


def cantidad_elementos(pila: Pila[int]) -> int:
    pila_aux = Pila()
    i : int = 0

    while not pila.empty():
        elemento = pila.get() # elemento = (obtener elementos de pila)
        pila_aux.put(elemento) # agregamos a pila_aux los elementos de la pila
        i += 1 # contamos los elementos que quitamos.

    while not pila_aux.empty(): # condicion para que nuestra pila_aux quede vacia.
        pila.put(pila_aux.get()) # agregamos los elementos de pila_aux 
    return i # devuelvo la cantidad de elementos


def mostrar_pila():
    pila = Pila()
    pila.put(10)
    pila.put(20)
    cantidad: int = cantidad_elementos(pila)
    return ("La pila:",print(list(pila.queue)),"Tiene",cantidad,"elementos.")

def buscar_el_maximo(p: Pila[int]) -> int:
    elemento_maximo = p.get() # sacamos un elemento de la pila.
    pila_aux: Pila[int] = Pila()

    while not p.empty(): # parte del requiere, la pila no debe ser vacia.
         elemento = p.get()
         pila_aux.put(elemento) # le agregamos los elementos a la pila.
          
         if elemento > elemento_maximo: # en el caso de que suceda esto.
             elemento_maximo = elemento   # guardamos el maximo en elem.max

    while not pila_aux.empty():
          p.put(pila_aux.get()) # reconstruimos nuestra pila.
    return elemento_maximo # devolvemos el maximo elemento.

def buscar_nota_maxima(p: Pila[tuple[str, int]]) -> tuple[str,int]:
    pila_aux: Pila[tuple[str, int]] = Pila()
    nota_maxima = p.get() # nota maxima seria tuple[str, int]

    while not p.empty(): # cuando la pila no esta vacia.
        elemento = p.get() 
        pila_aux.put(elemento) # le agregamos los elementos a pila_aux

        if elemento[1] > nota_maxima[1]: # y si la nota de elemento, es mayor a nota maxima
            nota_maxima = elemento # la nota maxima sera el elemento de pila.
    
    while not pila_aux.empty(): # vaciamos la pila aux
        p.put(pila_aux.get()) # dejamos nuestra pila original en forma base.

    return nota_maxima

def esta_bien_balanceada(sec: list[str]) -> bool:
    # s solo puede tener enteros, espacios y simbolos ( "(" , ")" ,"+","-","*","/")
    pila: Pila = Pila()

    for i in sec: # para cada elemento de la secuencia.
        if i == "(": # si nos encontramos con un (
            pila.put(i) # lo metemos a la pila.
        elif i == ")": # iteramos nuevamente, ignoramos (, y otro elemento.
            if pila.empty(): # si la pila esta vacia false, ya que no hay ( por comparar.
                return False
        pila.get() # quitamos cada ( por iteracion.
    return pila.empty() # si la pila queda vacia entonces esta balanceada.

def pila_ordenada(p: Pila[int]) -> bool:
    if p.empty():
        return True
    
    pila_aux: Pila[int] = Pila()
    anterior = p.get()
    pila_aux.put(anterior)

    while not p.empty():
        actual = p.get()
        pila_aux.put(actual)
        if actual < anterior:
            while not pila_aux.empty():
                p.put(pila_aux.get())
            return False
        anterior = actual
    
    while not pila_aux.empty():
        p.put(pila_aux.get())
    
    return True 

def intercalar(pila1: Pila[int], pila2: Pila[int]) -> Pila[int]:
    pila_intercalada: Pila[int] = Pila()
    pila_ordenada: Pila[int] = Pila()
    
    while not pila1.empty() and not pila2.empty():
        elementos_p1 = pila1.get()
        elementos_p2 = pila2.get()

        pila_intercalada.put(elementos_p1) 
        pila_intercalada.put(elementos_p2) 

    while not pila_intercalada.empty():
        pila_ordenada.put(pila_intercalada.get())

    return pila_ordenada

def generar_nros_azar(cantidad: int, desde: int, hasta: int) -> Cola[int]:
    cola: Cola[int] = Cola()

    for _ in range(1, cantidad):
        cola.put(random.randint(desde, hasta))
        cola.qsize() == cantidad

    return print(list(cola.queue))

def cantidad_elementos(c: Cola[int]) -> int:
    cola_aux: Cola[int] = Cola()
    i = 0

    while not c.empty(): # cola no vacia.
        elementos = c.get()
        cola_aux.put(elementos)
        i += 1
    
    while not cola_aux.empty():
        elementos_aux = cola_aux.get()
        c.put(elementos_aux)
    
    return i

def buscar_maximo(c: Cola[int]) -> int:

    cola_aux: Cola[int] = Cola()
    elemento_max = c.get()

    while not c.empty():
        elemento = c.get()
        cola_aux.put(elemento)
        if elemento_max < elemento:
            elemento_max = elemento

    while not cola_aux.empty():
        elemento_aux = cola_aux.get()
        c.put(elemento_aux)

    return elemento_max

def buscar_nota_minima(c: Cola[tuple[str, int]]) -> tuple[str, int]:

    cola_aux = Cola()
    nota_minima = c.get() # sacamos la tupla [str, int]. 
    cola_aux.put(nota_minima)

    while not c.empty():
        otras_notas = c.get()
        cola_aux.put(otras_notas)

        if otras_notas[1] < nota_minima[1]:
            nota_minima = otras_notas # igualamos el maximo al minimo.
        
    while not cola_aux.empty():
        elementos_aux = cola_aux.get()
        c.put(elementos_aux)
    
    return nota_minima

def intercalar(c1: Cola[int], c2: Cola[int]) -> Cola[int]:

    cola_aux: Cola[int] = Cola()

    while not c1.empty() and not c2.empty():    

        elementos_c1 = c1.get()
        elementos_c2 = c2.get()
        cola_aux.put(elementos_c1)
        cola_aux.put(elementos_c2)
    
    return cola_aux

def pacientes_urgentes(c: Cola[tuple[int, str, str]]) -> int: 

    cola_pacientes_graves = Cola()  # aca almacenare los casos en los que int  <= 4 (pacientes urgentes.)
    pacientes_riesgosos = c.get()
    cola_pacientes_graves.put(pacientes_riesgosos) # pacientes de alto riesgo.

    while not c.empty():
        pacientes = c.get()
     
        if pacientes[0] < pacientes_riesgosos[0] and pacientes[0] < 4:
            pacientes_riesgosos = pacientes
            cola_pacientes_graves.put(pacientes)
      
    return cantidad_elementos(cola_pacientes_graves)

nombre_apellido = str
DNI = int
tipo_cuenta = bool
prioridad = bool
Cliente = tuple[nombre_apellido, DNI, tipo_cuenta, prioridad]

def ordenar_clientes(c: Cola[Cliente]) -> Cola[Cliente]:
    cola_prioridad = Cola()
    cola_preferencial = Cola()
    cola_general = Cola()

    while not c.empty():
        cliente = c.get()
        if cliente[3]:
            cola_prioridad.put(cliente)
        elif cliente[2]:
            cola_preferencial.put(cliente)
        else: 
            cola_general.put(cliente)
    
    cola_ordenada = Cola()

    for cola in (cola_prioridad, cola_preferencial, cola_general):

        while not cola.empty():
            clientes = cola.get()
            cola_ordenada.put(clientes)

    return cola_ordenada

## diccionarios ## 

infoPaisFrancia = {'Capital': 'Paris', 'Campeonatos de Mundo' : 2}

def suma_elementos(s: list[float]) -> float:
    suma_total: float = 0
    for i in s:
        suma_total += i
    return suma_total

def calcular_promedio_por_estudiante(notas: list[tuple[str, float]]) -> dict[tuple[str, float]]:
    diccionario = {}
    # Primero guaradmos todas las notas de cada estudiante en listas.

    for nombre, nota in notas:
        if nombre not in diccionario:
            diccionario[nombre] = [nota] # inicializamos la lista.
        else:
            diccionario[nombre].append(nota) # si el nombre existe, agregamos una nueva nota a la lista.
        
    promedios = {}
    for nombre, lista_notas in diccionario.items():
        promedios[nombre] = suma_elementos(lista_notas) / len(lista_notas)

    return promedios



def visitar_sitio(historiales: dict[str, Pila[str]] , usuario: str, sitio: str):

    if usuario not in historiales:
        historiales[usuario] = Pila()
        historiales[usuario].put(sitio)

def navegar_atras(historiales: dict[str, Pila[str]], usuario: str) -> str:
    
    if usuario not in historiales:
       return None
    
    sitio_actual = historiales[usuario].get()
    return sitio_actual

from typing import Union
def agregar_producto(inventario: dict[str, dict[str, int|float]], nombre: str, precio: int|float, cantidad: int|float):
    categoria = "general"

    if categoria not in inventario: 
        inventario[categoria] = {} # creamos el inventario.

    inventario[categoria][nombre] = {"precio": precio, "cantidad": cantidad} 

#def actualizar_stock(inventario: dict[str, dict[str, int|float]], nombre: str, cantidad: int|float):





    

    
            
           
           


        






    














        









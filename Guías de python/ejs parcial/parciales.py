# Ejercicio 1 (2,25 puntos)
# Implementar la función subsecuencia_mas_larga especificada (todos_consecutivos no es testeado)

# problema subsecuencia_mas_larga (in v: seq⟨Z⟩) : ZxZ {
#   requiere: { La longitud de v es distinto de 0 }
#   asegura: { Sea x la primera subsecuencia más larga en v tal que vale todos_consecutivos(x), la primera componente de res es igual a |x| y la segunda es igual al índice en v donde comenzaría x }
# }

# problema todos_consecutivos (in v: seq⟨Z⟩) : Bool {
#   asegura: { res == True <==> cada par de elementos adyacentes en v son números consecutivos, es decir, que su diferencia es igual a 1 }
# }


# un ejemplo [1,2,3,4,5] -> es consecutivo, [4,5,6,7] -> es consecutivo [1,3,4,5] -> no es consecutivo.

def todos_consecutivos(sec: list[int]) -> bool:
    for n in range(len(sec) - 1):
        if sec[n + 1] - sec[n] != 1:
            return False
    return True

def subsecuencia_mas_larga(secuencia: list[int]) -> tuple[int, int]:
    subsecuencia: list[int] = []
    inicio: int = 0
    longitud_inicial: int = 0
    inicio_max: int = 0
    longitud_max: int = 0

    for i in range(len(secuencia)):
      subsecuencia.append(secuencia[i])
      if todos_consecutivos(subsecuencia):
          longitud_inicial += 1
          if longitud_inicial > longitud_max:
              longitud_max = longitud_inicial
              inicio_max = inicio
      else:
          inicio = i
          longitud_inicial = 1
          subsecuencia = [secuencia[i]]
    return tuple[longitud_max, inicio_max]
        
print(subsecuencia_mas_larga([1,2,3,4,5,0,1,2,3,4,5]))







        
                
        

            

        









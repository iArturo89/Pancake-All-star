from typing import List, Tuple, Union
from heapq import heappush, heappop

def heuristica(estado: List[str]) -> int:
    # Heurística: cuenta el número de "tortitas" desordenadas
    cuenta = 0
    for i in range(len(estado) - 1):
        if abs(ord(estado[i]) - ord(estado[i+1])) != 1:
            cuenta += 1
    return cuenta


def sucesores(estado: List[str]) -> List[Tuple[List[str], int]]:
    # Genera los sucesores del estado actual
    suces = []
    for i in range(2, len(estado) + 1):
        nuevo_estado = estado[:i][::-1] + estado[i:]
        costo = abs(i - len(estado))
        suces.append((nuevo_estado, costo))
    return suces


def ida_estrella(estado_inicial: List[int], estado_objetivo: List[int]) -> Tuple[List[int], int]:
    limite = heuristica(estado_inicial)
    camino = [estado_inicial]
    while True:
        t = busqueda(camino, 0, limite, estado_objetivo)
        if t == "ENCONTRADO":
            return camino, limite
        if t == float('inf'):
            return [], float('inf')
        limite = t

def busqueda(camino: List[List[int]], g: int, limite: int, estado_objetivo: List[int]) -> Union[str, int]:
    nodo = camino[-1]
    f = g + heuristica(nodo)
    if f > limite:
        return f
    if nodo == estado_objetivo:
        return "ENCONTRADO"
    min_costo = float('inf')
    for sucesor, costo in sucesores(nodo):
        if sucesor not in camino:
            camino.append(sucesor)
            t = busqueda(camino, g+costo, limite, estado_objetivo)
            if t == "ENCONTRADO":
                return "ENCONTRADO"
            if t < min_costo:
                min_costo = t
            camino.pop()
    return min_costo

# Ejemplo de uso:
estado_inicial = ['d', 'b', 'c', 'a']
estado_objetivo = ['a', 'b', 'c', 'd']
camino, costo = ida_estrella(estado_inicial, estado_objetivo)
print("Pasos:", len(camino) - 1)
print("Camino:", camino)
print("Costo:", costo)

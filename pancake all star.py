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


def a_estrella(estado_inicial: List[int], estado_objetivo: List[int]) -> Tuple[List[int], int]:
    abiertos = [(heuristica(estado_inicial), estado_inicial, 0)]
    cerrados = set()
    padres = {tuple(estado_inicial): None}
    costo_camino = {tuple(estado_inicial): 0}
    while abiertos:
        f, nodo, g = heappop(abiertos)
        if nodo == estado_objetivo:
            # Se llegó al objetivo, construir el camino y devolver
            camino = []
            while nodo:
                camino.append(nodo)
                nodo = padres[tuple(nodo)]
            return camino[::-1], costo_camino[tuple(camino[-1])]
        cerrados.add(tuple(nodo))
        for sucesor, costo in sucesores(nodo):
            if tuple(sucesor) in cerrados:
                continue
            nuevo_costo = costo_camino[tuple(nodo)] + costo
            if nuevo_costo < costo_camino.get(tuple(sucesor), float('inf')):
                costo_camino[tuple(sucesor)] = nuevo_costo
                f = nuevo_costo + heuristica(sucesor)
                heappush(abiertos, (f, sucesor, nuevo_costo))
                padres[tuple(sucesor)] = nodo
    return [], float('inf')

# Ejemplo de uso:
estado_inicial = ['d', 'b', 'c', 'a']
estado_objetivo = ['a', 'b', 'c', 'd']
camino, costo = a_estrella(estado_inicial, estado_objetivo)
print("Pasos:", len(camino) - 1)
print("Camino:", camino)
print("Costo:", costo)

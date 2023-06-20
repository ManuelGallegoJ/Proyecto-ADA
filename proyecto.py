import heapq

def dijkstra(grafo, inicio):
    camino = {nodo: (float('inf'), float('inf'), float('inf')) for nodo in grafo}
    # (tiempo acumulado, costo acumulado, valor de peso acumulado)
    camino[inicio] = (0, 0, 0)  
    # Cola de prioridad
    pq = [(0, inicio)]
    
    while pq:
        camino_actual, nodo_actual = heapq.heappop(pq)
        tiempo_actual, costo_actual, valor_estimado = camino[nodo_actual]
        
        # Si el nodo ya ha sido visitado, se omite
        if camino_actual > camino[nodo_actual][2]:
            continue
        
        for vecino, (tiempo, costo, estimado) in grafo[nodo_actual].items():
            total_tiempo = tiempo_actual + tiempo
            total_costo = costo_actual + costo
            total_estimado = valor_estimado + estimado
            # Si se encuentra un camino más corto hacia el vecino, se actualiza la distancia
            if (total_estimado) < camino[vecino][2]:
                camino[vecino] = (total_tiempo, total_costo, total_estimado)
                heapq.heappush(pq, (total_estimado, vecino))
    
    return camino

# Ejemplo de uso:

# Creo el grafo de ejemplo
grafo = {
    'A': {'B': (5, 0, 5), 'C': (2, 0, 2)},
    'B': {'D': (3, 2, 5), 'A': (5, 0, 5), 'C': (1, 0, 1)},
    'C': {'B': (1, 0, 1), 'D': (6, 4, 10), 'A': (2, 0, 2)},
    'D': {'E': (8, 5, 13), 'C': (6, 4, 10), 'B': (3, 2, 5)},
    'E': {'D': (8, 5, 13)}
}

#Nodo de partida
inicio_nodo = 'A'

camino = dijkstra(grafo, inicio_nodo)


print(camino)
# Imprimimos los caminos que cumplen el nodo de origen, imprimo todos para analizar, luego se cambiará
for nodo, (tiempo, costo, valor) in camino.items():
    print(f"Distancia más corta desde {inicio_nodo} hasta {nodo}: tiempo={tiempo}, costo={costo}, valor={valor}")





#while True:
#    #caso a probar. Si se ingresa cero, finaliza la ejecucion
#    caso = input()
#    if caso == "0":
#        break

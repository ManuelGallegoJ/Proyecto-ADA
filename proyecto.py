import heapq

def dijkstra(grafo, nodo_inicial):
    # En este caso se utilizará set() porque tiene un O(1) promedio para:
    # agregar add()
    # eliminar remove() o discard()
    # buscar elementos in
    # Variable en la que se almacenan los nodos que no se han analizado
    nodos_no_visitados = set(i for i in grafo)
    # Variable que va a almacenar la información de las rutas, al inicio no sabemos nada, por eo los inf
    # tabla = {nodo: [[tiempo, costo, valor], anterior camino], ... }
    tabla = {nodo_no_visitado: [[float("inf"), float("inf"), float("inf")], None] for nodo_no_visitado in nodos_no_visitados}
    tabla[nodo_inicial] = [[0, 0, 0], None]
    # Nodo en el que se encuentra en este momento
    nodo_actual = nodo_inicial
    tiempo_acumulado = 0
    costo_acumulado = 0
    valor_acumulado = 0
    # Cola de prioridad para almacenar los nodos no visitados
    cola_prioridad = [(0, nodo_inicial)]
    heapq.heapify(cola_prioridad)
    
    while cola_prioridad:
        # Extrae el nodo de menor valor acumulado de la cola de prioridad
        _, nodo_actual = heapq.heappop(cola_prioridad)  
        # Verifica que el nodo no haya sido visitado antes
        if nodo_actual in nodos_no_visitados:  
            # Marca el nodo actual como visitado
            nodos_no_visitados.remove(nodo_actual)
            # Explora los vecinos del nodo actual
            for j in grafo[nodo_actual]: 
                # Compara el valor acumulado actual con el valor en la tabla
                if grafo[nodo_actual][j][2] < tabla[j][0][2]:  
                    tiempo_acumulado = tabla[nodo_actual][0][0] + grafo[nodo_actual][j][0]
                    costo_acumulado = tabla[nodo_actual][0][1] + grafo[nodo_actual][j][1]
                    valor_acumulado = tabla[nodo_actual][0][2] + grafo[nodo_actual][j][2]
                    # Actualiza la tabla si el nuevo valor acumulado es menor
                    if valor_acumulado < tabla[j][0][2]:  
                        tabla[j] = [[tiempo_acumulado, costo_acumulado, valor_acumulado], nodo_actual]
                        # Agrega el nodo a la cola de prioridad
                        heapq.heappush(cola_prioridad, (valor_acumulado, j))  
    return tabla

# Ejemplo de uso:
# Creo el grafo de ejemplo
#grafo = {
#    "A": {"B": (1, 1, 2), "D": (0, 8, 8)},
#    "B": {"E": (3, 3, 6), "D": (1, 4, 5), "A": (1, 1, 2)},
#    "C": {"E": (6, 3, 9), "F": (1, 2, 3)},
#    "D": {"F": (1, 1, 2), "E": (0, 3, 3), "B": (1, 4, 5), "D": (0, 8, 8)},
#    "E": {"F": (0, 1, 1), "C": (6, 3, 9), "B": (3, 3, 6), "D": (0, 3, 3)},
#    "F": {"E": (0, 1, 1), "C": (1, 2, 3), "D": (1, 1, 2)}
#}

# Importancia que se le da al tiempo y al costo
peso_tiempo = float(input("Ingrese el peso que va a tener el tiempo [0, 1]: "))     # Valor en el rango de [0, 1]
peso_costo = float(input("Ingrese el peso que va a tener el costo [0, 1]: "))      # Valor en el rango de [0, 1]
grafo = {}

while True:
    #Si se ingresa cero, finaliza la ejecucion
    caso = input("Ingrese la conexión entre nodo (todas): ")
    if caso == "0":
        break

    # Separa los datos para manejarlos más cómodo
    caso = caso.split()
    actual = caso[0]
    va_a = caso[1]
    tiempo_de = int(caso[2])
    costo_de = int(caso[3])
    valor_calculado = tiempo_de*peso_tiempo + costo_de*peso_costo
    # Se ve si el nodo existe, en caso de no existir lo crea

    for _ in range(2):
        if actual in grafo:
            # Se ve si la conexión no existe para crearla, si existe compara y deja la que tenga un valor_calculado menor 
            if not(va_a in grafo[actual]):
                grafo[actual][va_a] = tiempo_de, costo_de, valor_calculado
            # Reemplazo si tiene un valor menor
            elif valor_calculado < grafo[actual][va_a][2]:
                grafo[actual][va_a] = tiempo_de, costo_de, valor_calculado
        else:
            grafo_auxiliar = {va_a: (tiempo_de, costo_de, valor_calculado)}
            grafo[actual] = grafo_auxiliar
        actual = caso[1]
        va_a = caso[0]


#Nodo de partida
nodo_inicial = input("Ingrese el punto de partida: ")
#Nodo destino
destino = input("Ingrese el punto de destino: ")
aux_destino = destino
camino = dijkstra(grafo, nodo_inicial)
ruta = ""

while True:
    # Creo la cadena que va a tener el camino a seguir
    ruta += aux_destino + " >-- "
    aux_destino = camino[aux_destino][1]
    if aux_destino == nodo_inicial:
        ruta += nodo_inicial
        ruta = ruta[::-1]
        break

print(f"La ruta óptima según nuestra necesidad es: {ruta}")
print(f"Esta ruta demora: {camino[destino][0][0]} minutos.")
print(f"Esta ruta tiene un costo de: {camino[destino][0][1]}")

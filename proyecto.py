def dijstra(grafo, nodo_inicial):
    # En este caso se utilizará set() porque tiene un O(1) promedio para:
    # agregar add()
    # eliminar remove() o discard()
    # buscar elementos in
    # Variable en la que almacenan los nodos analizados
    nodos_visitados = set()
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
    # Recorrer
    for i in range(len(nodos_no_visitados)):
        # Recorro los vecinos del nodo actual
        for j in grafo[nodo_actual]:
            # Comparo si el valor actual es menor que el de la tabla
            if grafo[nodo_actual][j][2] < tabla[j][0][2] and j in nodos_no_visitados:
                tiempo_acumulado = tabla[nodo_actual][0][0] + grafo[nodo_actual][j][0]
                costo_acumulado = tabla[nodo_actual][0][1] + grafo[nodo_actual][j][1]
                valor_acumulado = tabla[nodo_actual][0][2] + grafo[nodo_actual][j][2]
                # Comparo si el valor acumulado es menor que el de la tabla
                if valor_acumulado < tabla[j][0][2]:
                    tabla[j] = [[tiempo_acumulado, costo_acumulado, valor_acumulado], nodo_actual]

        nodos_no_visitados.remove(nodo_actual)
        nodos_visitados.add(nodo_actual)
        # Debo buscar en tabla el nodo no visitado con el valor más pequeño     
        # Esto sir ve para seleccionar al siguiente nodo
        menor = float("inf")
        nodo_menor = ""
        for k in nodos_no_visitados:
            if menor > tabla[k][0][2]:
                menor = tabla[k][0][2]
                nodo_menor = k
        nodo_actual = nodo_menor
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
peso_tiempo = int(input("Ingrese el peso que va a tener el tiempo [0, 1]: "))     # Valor en el rango de [0, 1]
peso_costo = int(input("Ingrese el peso que va a tener el costo [0, 1]: "))      # Valor en el rango de [0, 1]
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

#Nodo de partida
nodo_inicial = input("Ingrese el punto de partida: ")
#Nodo destino
destino = input("Ingrese el punto de destino: ")
aux_destino = destino
camino = dijstra(grafo, nodo_inicial)
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
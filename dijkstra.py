graph = {

'1':{'2':2, '3':1},
'2':{'4':3, '5':4},
'3':{'4':2, '5':6},
'4':{'6':7},
'5':{'6':8},
'6':{}

}

def dijkstra(graph, start, goal):
    shortest_distance = {} # armazena o custo para chegar naquele vértice. Vai mudar conforme avançamnos no grafo
    track_predecessor = {} # armazena o caminho que levou para esse vértice
    unseenNodes = graph 
    infinity = 999999 # só um numero grandão mesmo, pra representar os vértices no começo
    track_path = [] # vai manter a nossa jornada de volta para o vértice inicial
    
    for node in unseenNodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseenNodes:

        min_distance_node = None

        for node in unseenNodes:
            if min_distance_node is None:
                min_distance_node = node
            elif shortest_distance[node] < shortest_distance[min_distance_node]:
                min_distance_node = node

        path_options = graph[min_distance_node].items()

        for child_node, weight in path_options:

            if weight + shortest_distance[min_distance_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_distance_node]
                track_predecessor[child_node] = min_distance_node

        unseenNodes.pop(min_distance_node)

    currentNode = goal

    while currentNode != start:
        try:
            track_path.insert(0, currentNode)
            currentNode = track_predecessor[currentNode]

        except KeyError:
            print("Caminho não alcansavel")
            break

    track_path.insert(0, start)


    if shortest_distance[goal] != infinity:
        print("O caminho mais curto é " + str(shortest_distance[goal]))
        print("O caminho mais otimizado é" + str(track_path))

dijkstra(graph, '1', '6')

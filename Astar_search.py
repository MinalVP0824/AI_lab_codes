import matplotlib.pyplot as plt
import networkx as nx
import heapq

def astar(graph, heuristic, start, goal):
    heap = [(heuristic[start], 0, start, [start])]
    visited = set()

    while heap:
        f, g, node, path = heapq.heappop(heap)
        if node in visited:
            continue 
        visited.add(node)
        
        if node == goal:
            print("Path: ", path)
            print("Cost: ", g)
            return path
        
        for neighbor, weight in graph.get(node, []):
            if neighbor not in visited:
                new_g = g + weight
                new_f = new_g + heuristic.get(neighbor,0)
                heapq.heappush(heap, (new_f, new_g, neighbor, path + [neighbor]))
    
    print("No solution found.")
    return None

def draw_graph(graph, path = None):

    G = nx.DiGraph()

    for node, neighbours in graph.items():
        for neighbour, weight in neighbours:
            G.add_edge(node, neighbour, weight = weight)

    pos = nx.spring_layout(G, seed=42)

    path_edges = list(zip(path, path[1:])) if path else []
    node_colors = ['lightgreen' if n in path else 'lightblue' for n in G.nodes()]

    plt.figure(figsize=(8,6))

    nx.draw(G, pos, with_labels=True, node_color= node_colors, node_size=2000, font_size= 15, font_weight="bold", edge_color="gray")
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u,v):d['weight'] for u, v, d in G.edges(data = True)})

    if path_edges:
        nx.draw_networkx_edges(G, pos, edgelist= path_edges, edge_color='red', width=3)
    
    plt.title("A* search Algorithm")
    plt.show()

graph = {
    'A': [('B', 2), ('E', 3)],
    'B': [('C', 1), ('G', 9)],
    'C': [],
    'E':[('D', 6)],
    'D': [('G', 1)],
    'G':[]
}

heuristic = {
    'A' : 11,
    'B':6,
    'C': 99,
    'D': 1,
    'E': 7,
    'G': 0
    }

path = astar(graph, heuristic, 'A', 'G')
draw_graph(graph, path)
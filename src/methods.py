import math
from collections import deque
import heapq

def find_bfs_path(G, source, target):
    # Initialize the queue with the source node and the path as a list containing the source node
    queue = deque([(source, [source])])
    visited = set()

    while queue:
        # Pop the node and path from the queue
        current_node, path = queue.popleft()
        
        # If the current node is the target, return the path
        if current_node == target:
            return path
        
        # Mark the current node as visited
        visited.add(current_node)
        
        # Explore neighbors
        for neighbor in G.neighbors(current_node):
            if neighbor not in visited:
                # Append the neighbor and the new path to the queue
                queue.append((neighbor, path + [neighbor]))
    
    # If no path is found
    return None

def find_dfs_path(G, source, target):
    stack = [source]
    visited = set()
    predecessors = {}

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.add(node)
            if node == target: break
            x, y = node
            directions = [
                (x-1, y), # N
                (x, y-1), # W
                (x, y+1), # E
                (x+1, y) # S
            ]
            neighbors = [n for n in G.neighbors(node) if n not in visited]
            sorted_neightbors = sorted(neighbors, key=lambda n: directions.index(n) if n in directions else float('inf'))
            for direction in directions:
                for neighbor in neighbors:
                    sorted_neightbors.append(neighbor) if direction == neighbor else None
            for neighbor in sorted_neightbors:
                if neighbor not in visited and neighbor not in stack:
                    stack.append(neighbor)
                    predecessors[neighbor] = node
    path = [target]
    while target in predecessors:
        target = predecessors[target]
        path.append(target)
    path.reverse()

    return path

def Manhattan(u, v):
    (x1, y1) = (u[0], u[1])
    (x2, y2) = (v[0], v[1])
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return (dx + dy)

def Chebyshev(u, v):
    (x1, y1) = (u[0], u[1])
    (x2, y2) = (v[0], v[1])
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return max(dx, dy)

def Euclidian(u, v):
    (x1, y1) = (u[0], u[1])
    (x2, y2) = (v[0], v[1])
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return math.sqrt(dx * dx + dy * dy)

def Euclidian_squared(u, v):
    (x1, y1) = (u[0], u[1])
    (x2, y2) = (v[0], v[1])
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return (dx * dx + dy * dy)

def astar_shortest_path(G, source, target, heuristic):
    # Inicializa a fila de prioridade com o nó de origem
    queue = [(0, source)]
    # Dicionário para armazenar o custo total mínimo de chegar a cada nó
    g_costs = {source: 0}
    # Dicionário para armazenar o caminho
    predecessors = {source: None}

    while queue:
        # Extrai o nó com o menor custo estimado (f(n) = g(n) + h(n))
        current_cost, current_node = heapq.heappop(queue)

        # Se alcançou o destino, reconstrua o caminho
        if current_node == target:
            path = []
            while current_node:
                path.append(current_node)
                current_node = predecessors[current_node]
            path.reverse()
            return path

        # Explora os vizinhos do nó atual
        for neighbor in G.neighbors(current_node):
            tentative_g_cost = g_costs[current_node] + G[current_node][neighbor].get('weight', 1)
            
            # Se o custo estimado para o vizinho é menor, ou ainda não foi visitado
            if neighbor not in g_costs or tentative_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, target)
                heapq.heappush(queue, (f_cost, neighbor))
                predecessors[neighbor] = current_node

    # Se nenhum caminho for encontrado, retorna None
    return None
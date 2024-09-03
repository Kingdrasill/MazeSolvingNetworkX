import math

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
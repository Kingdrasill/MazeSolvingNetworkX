import pyamaze as pm
import networkx as nx
import ast as at
import math

def find_dfs_path(G, source, target):
    predecessors = nx.dfs_predecessors(G, source)
    path = [target]
    while target != source:
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

size = 51
# Generate random start and finish positions
start_position = (1, 1)
finish_position = (size, size)

# Create the maze
m = pm.maze(size, size)

f = open(f"mazes/test-maze.txt", "w")  

# Create the maze with the random finish position
m.CreateMaze(finish_position[0], finish_position[1], loopPercent=20, theme='light')
# Write the maze details to the file
string = f"{start_position[0]},{start_position[1]} - {finish_position[0]},{finish_position[1]}\n"
for key in m.maze_map.keys():
    string += f"{key[0]},{key[1]} & {m.maze_map[key]} $ "
string = string[:-2]

# Save to the file
f.write(string)
f.close()

file = open(f"mazes/test-maze.txt", "r")

G = nx.Graph()
positions = file.readline().strip().split('-')
positions = [position.strip() for position in positions]
start = tuple(map(int , positions[0].split(',')))
finish = tuple(map(int , positions[1].split(',')))
nodes = file.read().split('$')
keys = list()
adjacents = list()
for node in nodes:
    node = node.replace(' ', '').split('&')
    keys.append(tuple(map(int , node[0].split(','))))
    adjacents.append(at.literal_eval(node[1]))

file.close() 

G.add_nodes_from(keys)
for node, adjacent in zip(keys, adjacents):
    for key in adjacent.keys():
        if adjacent[key]:
            match (key):
                case 'N':
                    G.add_edge(node, (node[0]-1, node[1]), weight = 1)
                case 'W':
                    G.add_edge(node, (node[0], node[1]-1), weight = 1)
                case 'S':
                    G.add_edge(node, (node[0]+1, node[1]), weight = 1)
                case 'E':
                    G.add_edge(node, (node[0], node[1]+1), weight = 1)

bfs_color = 'red'
dfs_color = 'blue'
manhattan_color = 'green'
chebyshev_color = 'yellow'
euclidiana_color = 'black'
euclidiana2_color = 'cyan'

bfs = pm.agent(m, footprints=True, color=bfs_color)
dfs = pm.agent(m, footprints=True, color=dfs_color)
manhattan = pm.agent(m, footprints=True, color=manhattan_color)
chebyshev = pm.agent(m, footprints=True, color=chebyshev_color)
euclidiana = pm.agent(m, footprints=True, color=euclidiana_color)
euclidiana2 = pm.agent(m, footprints=True, color=euclidiana2_color)

bfs.position = start
dfs.position = start
manhattan.position = start
chebyshev.position = start
euclidiana.position = start
euclidiana2.position = start

bfs_path = nx.shortest_path(G, source=start, target=finish)
dfs_path = find_dfs_path(G, start, finish)
manhattan_path = nx.astar_path(G, source=start, target=finish, heuristic=lambda u, v: Manhattan(u, v), weight='weight')
chebyshev_path = nx.astar_path(G, source=start, target=finish, heuristic=lambda u, v: Chebyshev(u, v), weight='weight')
euclidiana_path = nx.astar_path(G, source=start, target=finish, heuristic=lambda u, v: Euclidian(u, v), weight='weight')
euclidiana2_path = nx.astar_path(G, source=start, target=finish, heuristic=lambda u, v: Euclidian_squared(u, v), weight='weight')

m.tracePath({
        bfs: bfs_path
    }, delay=10)

m.tracePath({
        manhattan: manhattan_path
    }, delay=10)

m.tracePath({ 
        chebyshev: chebyshev_path
    }, delay=10)

m.tracePath({
        euclidiana: euclidiana_path
    }, delay=10)

m.tracePath({
        euclidiana2: euclidiana2_path
    }, delay=10)

m.tracePath({
        dfs: dfs_path
    }, delay=10)

pm.textLabel(m, 'BFS', 'Vermelho')
pm.textLabel(m, 'DFS', 'Azul')
pm.textLabel(m, 'A* - Manhattan', 'Verde')
pm.textLabel(m, 'A* - Chebyshev', 'Amarelo')
pm.textLabel(m, 'A* - Euclidiana', 'Preto')
pm.textLabel(m, 'A* - Euclidiana^2', 'Ciano')

m.run()
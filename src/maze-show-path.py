import pyamaze as pm
import networkx as nx
import methods as mt
from sys import argv

size = int(argv[1])

start = (1, 1)
finish = (size, size)

m = pm.maze(size, size)
m.CreateMaze(finish[0], finish[1], loopPercent=20, theme='light')

G = nx.Graph()

for node in m.maze_map.keys():
    G.add_node(node)

for node, directions in zip(m.maze_map.keys(), m.maze_map.values()):
    for direction in directions:
        if m.maze_map[node][direction]:
            match direction:
                case 'S':
                    G.add_edge(node, (node[0]+1, node[1]))
                case 'N':
                    G.add_edge(node, (node[0]-1, node[1]))
                case 'E':
                    G.add_edge(node, (node[0], node[1]+1))
                case 'W':
                    G.add_edge(node, (node[0], node[1]-1))

bfs_color = 'red'
dfs_color = 'blue'
manhattan_color = 'green'
chebyshev_color = 'yellow'
euclidiana_color = 'black'
euclidiana2_color = 'cyan'

bfs = pm.agent(m, footprints=True, color=bfs_color, filled=True)
dfs = pm.agent(m, footprints=True, color=dfs_color, filled=True)
manhattan = pm.agent(m, footprints=True, color=manhattan_color, filled=True)
chebyshev = pm.agent(m, footprints=True, color=chebyshev_color, filled=True)
euclidiana = pm.agent(m, footprints=True, color=euclidiana_color, filled=True)
euclidiana2 = pm.agent(m, footprints=True, color=euclidiana2_color, filled=True)

bfs.position = start
dfs.position = start
manhattan.position = start
chebyshev.position = start
euclidiana.position = start
euclidiana2.position = start

bfs_path = mt.find_bfs_path(G, source=start, target=finish)
dfs_path = mt.find_dfs_path(G, start, finish)
manhattan_path = mt.astar_shortest_path(G, source=start, target=finish, heuristic=mt.Manhattan)
chebyshev_path = mt.astar_shortest_path(G, source=start, target=finish, heuristic=mt.Chebyshev)
euclidiana_path = mt.astar_shortest_path(G, source=start, target=finish, heuristic=mt.Euclidian)
euclidiana2_path = mt.astar_shortest_path(G, source=start, target=finish, heuristic=mt.Euclidian_squared)

m.tracePath({
    bfs: bfs_path
}, delay=30)

m.tracePath({
    dfs: dfs_path
}, delay=30)

m.tracePath({
    manhattan: manhattan_path
}, delay=30)

m.tracePath({ 
    chebyshev: chebyshev_path
}, delay=30)

m.tracePath({
    euclidiana: euclidiana_path
}, delay=30)

m.tracePath({
    euclidiana2: euclidiana2_path
}, delay=30)

pm.textLabel(m, 'BFS', 'Vermelho')
pm.textLabel(m, 'DFS', 'Azul')
pm.textLabel(m, 'A* - Manhattan', 'Verde')
pm.textLabel(m, 'A* - Chebyshev', 'Amarelo')
pm.textLabel(m, 'A* - Euclidiana', 'Preto')
pm.textLabel(m, 'A* - Euclidiana^2', 'Ciano')

m.run()
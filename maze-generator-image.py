import pyamaze as pm
import random

sizes = [11, 21, 31, 41, 51]

for size in sizes:    
    # Create the maze
    m = pm.maze(size, size)
    
    # Generate random start and finish positions
    start_position = (random.randint(1, size), random.randint(1, size))
    finish_position = (random.randint(1, size), random.randint(1, size))
    
    # Ensure that start and finish are not the same
    while start_position == finish_position:
        finish_position = (random.randint(1, size), random.randint(1, size))
    
    # Create the maze with the random finish position
    m.CreateMaze(finish_position[0], finish_position[1], loopPercent=20, theme='light')
    a = pm.agent(m)
    a.position = start_position

    m.run()
from pyamaze import maze, agent

sizes = [11, 21, 31, 41, 51]

for size in sizes:        
    # Create the maze
    m = maze(size, size)
    
    # Generate random start and finish positions
    start_position = (1, 1)
    finish_position = (size, size)
    
    # Create the maze with the random finish position
    m.CreateMaze(finish_position[0], finish_position[1], loopPercent=20, theme='light')
    
    a = agent(m, footprints=True, color='red', filled=True)
    a.position = start_position

    m.run()

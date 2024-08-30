from pyamaze import maze
import random
from sys import argv

sizes = [11, 21, 31, 41, 51]

for size in sizes:
    for i in range(int(argv[1])):
        f = open(f"mazes/{size}/{i+1}.txt", "w")
        
        # Create the maze
        m = maze(size, size)
        
        # Generate random start and finish positions
        start_position = (random.randint(1, size), random.randint(1, size))
        finish_position = (random.randint(1, size), random.randint(1, size))
        
        # Ensure that start and finish are not the same
        while start_position == finish_position:
            finish_position = (random.randint(1, size), random.randint(1, size))
        
        # Create the maze with the random finish position
        m.CreateMaze(finish_position[0], finish_position[1], loopPercent=20)
        
        # Write the maze details to the file
        string = f"{start_position[0]},{start_position[1]} - {finish_position[0]},{finish_position[1]}\n"
        for key in m.maze_map.keys():
            string += f"{key[0]},{key[1]} & {m.maze_map[key]} $ "
        string = string[:-2]
        
        # Save to the file
        f.write(string)
        f.close()
        
        del m

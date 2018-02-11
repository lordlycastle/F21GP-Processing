from __future__ import division

maze = None
maze_size = 30

fps = 30
time_step = 1 / fps

blocked_color = color(255, 0, 0)
open_color = color(0, 255, 0)
block_size = 20

def setup():
    global maze
    size(maze_size*block_size, maze_size*block_size)
    frameRate(fps)
    
    noiseSeed(minute() * second())
    maze = generate_maze(size=maze_size, 
                         probability_of_blocked=0.2)
    

def draw():
    global maze
    draw_maze(maze)


def generate_maze(size=20, probability_of_blocked=0.3, min_blocked=80):
    maze = []
    blocked_count = 0
    for _ in range(size):
        row = [0] * size
        maze.append(row)
    for x in range(size):
        for y in range(size):
            blocked = noise(x, y) < probability_of_blocked
            blocked_count += 1 if blocked else 0
            maze[x][y] = 1 if blocked else 0

    if not blocked_count > min_blocked:
        return generate_maze(size=size,
                            probability_of_blocked=probability_of_blocked * 1.1,
                            min_blocked=min_blocked)
    return maze


def draw_maze(maze):
    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 1:
                fill(blocked_color)
            elif maze[x][y] == 0:
                fill(open_color)
            
            rect((x) * 20, y * 20, block_size, block_size)

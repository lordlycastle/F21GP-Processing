from __future__ import division
from vector3 import Vector3
from path_finder import AStar

maze = None
maze_size = 20

fps = 20
time_step = 1 / fps

blocked_block = 1
open_block = 0
block_size = 30
blocked_color = color(255, 0, 0)
open_color = color(0, 255, 0)
player_color = color(0, 0, 255)
target_color = color(244, 66, 226)
path_color = color(0, 0, 255, 150)
explored_color = '#F08A4B'
draw_solution = False

# Will only need x,y
player_location = Vector3()
target_location = Vector3()

astar = 0

def setup():
    size(maze_size * block_size, maze_size * block_size)
    # frameRate(fps)
    noLoop()
    
    
    new_maze()

def new_maze():
    global maze, player_location, target_location, astar
    noiseSeed(minute() * second() * millis())
    randomSeed(millis() * second() * minute())
    
    maze = generate_maze(size=maze_size,
                         # probability_of_blocked=0.4,
                         probability_of_blocked=0.3,
                         min_blocked=maze_size*maze_size*0.2 
                         )
    
    player_location.x, player_location.y = get_spawn_location(maze)
    target_location.x, target_location.y = get_spawn_location(maze)
    while player_location == target_location:
        target_location.x, target_location.y = get_spawn_location(maze)
    print('Player: ' + str(player_location))
    print('Target: ' + str(target_location))
    
    astar = AStar(maze=maze, start_coord=player_location, target=target_location)

def draw():
    global maze, player_location, target_location, astar, draw_solution
    draw_maze(maze)
    draw_player(player_location)
    draw_target(target_location)
    if draw_solution:
        draw_explored(astar)
        draw_path(astar)
        draw_solution = False
        
    print('----------------')
    

def keyPressed():
    global maze, astar, draw_solution
    if key == 'u':
        new_maze()
        redraw()
        
    if key == 'p':
        astar.find_path()
        for y in range(len(maze)):
            cl = ''
            for x in range(len(maze[0])):
                cl += str(astar.node_map[y][x]) + ', '
            print(cl)
            
    if key == 'f':
        astar.find_path(allow_diagonal=False)
        draw_solution = True
        redraw()
        

def generate_maze(size=20, probability_of_blocked=0.3, min_blocked=80):
    global blocked_block, open_block
    if size*size <= min_blocked+2:
        min_blocked = int(probability_of_blocked * size*size)
        print('Had to change min number of blocked blocks to: '+str(min_blocked))
    maze = []
    blocked_count = 0
    for _ in range(size):
        row = [0] * size
        maze.append(row)
    for x in range(size):
        for y in range(size):
            blocked = noise(y, x) < probability_of_blocked
            blocked_count += 1 if blocked else 0
            maze[y][x] = blocked_block if blocked else open_block

    if not blocked_count > min_blocked and probability_of_blocked != 0:
        return generate_maze(size=size,
                             probability_of_blocked=probability_of_blocked *
                             1.1,
                             min_blocked=min_blocked)
    
    print('\nMaze: {}x{}, Blocked: {}'.format(size, size, blocked_count))
    # printArray(maze)
    return maze


def draw_maze(maze):
    global open_block, blocked_block
    for x in range(len(maze[0])):
        for y in range(len(maze)):
            if maze[y][x] == blocked_block:
                fill(blocked_color)
            elif maze[y][x] == open_block:
                fill(open_color)
            
            rect((x) * block_size, y * block_size, block_size, block_size)

def get_spawn_location(maze):
    global open_block
    
    spawn_location_x = int(random(0, len(maze[0])))
    spawn_location_y = int(random(0, len(maze)))
    if maze[spawn_location_y][spawn_location_x] != open_block:
        return get_spawn_location(maze)
    return spawn_location_x, spawn_location_y
    
def draw_player(player_location):
    fill(player_color)
    ellipse(player_location.x * block_size + 0.5 * block_size,
            player_location.y * block_size + 0.5 * block_size,
            block_size / 2,
            block_size / 2)
    
def draw_target(target_location):
    fill(target_color)
    rect(target_location.x * block_size + block_size * 0.1,
         target_location.y * block_size + block_size * 0.1,
         block_size * 0.8,
         block_size * 0.8,
         block_size)
    
def draw_path(astar):
    fill(path_color)
    final_node = astar.node_map[astar.target.y][astar.target.x]
    while True:
        if final_node == None:
            return
        rect(final_node.x *block_size,
             final_node.y * block_size,
             block_size, 
             block_size)
        final_node = final_node.parent
        
def draw_explored(astar):
    fill(explored_color)
    for y in range(len(astar.maze)):
        for x in range(len(astar.maze[0])):
            if astar.node_map[y][x] == None:
                continue
            node = astar.node_map[y][x]
            if node.explored and not node.opened:
                rect(node.x * block_size,
                     node.y * block_size,
                     block_size,
                     block_size)
                
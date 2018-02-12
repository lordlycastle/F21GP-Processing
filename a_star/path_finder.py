from vector3 import Vector3

class AStar(object):

    def __init__(self, maze, start_coord, target):
        self.maze = maze
        self.start_coord = start_coord
        self.target = target
        self.node_map = []
        self.open_block = 0
        self.blocked_block = 1

        self.start_node = None
        # self.open_nodes = []
        # self.closed_nodes = []
    
    def create_node_map(self):
        self.node_map = []
        for y in range(len(self.maze)):
            node_row = []
            for x in range(len(self.maze[0])):
                if self.maze[y][x] == self.blocked_block:
                    node_row.append(None)
                else:
                    node = Node(x=x, y=y)
                    node_row.append(node)
            self.node_map.append(node_row)
            

    def find_path(self, allow_diagonal=True):
        count = 0
        self.create_node_map()
        self.start_node = self.node_map[self.start_coord.y][self.start_coord.x]
        self.start_node.opened = True
        open_nodes = [self.start_node]
        closed_nodes = []
        while True:
            current_node = self.get_current_node(open_nodes)
            open_nodes.remove(current_node)
            current_node.explored = True
            closed_nodes.append(current_node)

            if current_node.x == self.target.x and \
               current_node.y == self.target.y:
                break

            neighbourhood = current_node.get_neighbourhood_locations(allow_diagonal)
            neighbourhood = self.check_neighbourhood_boundary(neighbourhood)
            for neighbour in neighbourhood:
                neighbour_node = self.node_map[neighbour.y][neighbour.x]
                if neighbour_node == None:
                    continue
                elif neighbour_node.explored:
                    continue

                g_cost = neighbour_node.get_g_cost_from(current_node.x,
                                                        current_node.y)
                if not neighbour_node.opened or \
                        current_node.g_cost + g_cost < neighbour_node.g_cost:
                    neighbour_node.g_cost = current_node.g_cost + g_cost
                    neighbour_node.set_h_cost_to(self.target.x, self.target.y)
                    neighbour_node.parent = current_node
                    neighbour_node.opened = True
                    open_nodes.append(neighbour_node)

            count += 1
            if count > 10000:
                print("Stuck in a loop")
                break
            
        print('Moves: '+str(count))

    def check_neighbourhood_boundary(self, neighbourhood):
        x_len = len(self.maze[0])-1
        y_len = len(self.maze)-1
        new_neighbourhood = []
        for coord in neighbourhood:
            if coord.x > x_len or coord.y > y_len or \
                coord.x < 0 or coord.y < 0:
                continue
            new_neighbourhood.append(coord)
        return new_neighbourhood
    
    def get_current_node(self, open_nodes):
        min_f_cost = 99999999999
        lowest_node = None
        for node in open_nodes:
            if node.f_cost < min_f_cost:
                lowest_node = node
                min_f_cost = lowest_node.f_cost
        if lowest_node == None:
            print('Error: No starting point. Count: '+str(len(open_nodes)))
        return lowest_node

class Node(object):

    def __init__(self, x, y, g_cost=0, h_cost=0, parent=None):
        self.x = x
        self.y = y
        self.g_cost = g_cost
        self.h_cost = h_cost
        self.parent = parent
        self.explored = False
        self.straight_cost = 10
        self.diagonal_cost = 14
        self.opened = False

    @property
    def f_cost(self):
        return self.g_cost + self.h_cost

    def get_neighbourhood_locations(self, get_diagonal=True):
        neighbourhood = [Vector3(self.x + 1, self.y),
                         Vector3(self.x, self.y + 1),
                         Vector3(self.x - 1, self.y),
                         Vector3(self.x, self.y - 1),
                         ]
        if get_diagonal:
            neighbourhood.append(Vector3(self.x + 1, self.y + 1))
            neighbourhood.append(Vector3(self.x + 1, self.y - 1))
            neighbourhood.append(Vector3(self.x - 1, self.y + 1))
            neighbourhood.append(Vector3(self.x - 1, self.y - 1))

        return neighbourhood

    def get_g_cost_from(self, x, y):
        if self.x == x or self.y == y:
            return self.straight_cost
        else:
            return self.diagonal_cost

    def set_h_cost_to(self, x, y):
        self.h_cost = (abs(self.x - x) + abs(self.y - y)) * 10

    def __str__(self):
        return 'G: {: >3}, H:{: >3}, ({},{})'.format(self.g_cost, self.h_cost,
                                                 self.x, self.y)
import pygame
from grid import Grid
class Maze:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Maze")
        self.RES = 600
        self.dis = pygame.display.set_mode((self.RES + 20, self.RES + 20))
        self.dis.fill('ivory')
        self.grid_size = 10
        self.cell_size = self.RES / self.grid_size
        self.maze = Grid(self.grid_size, self.grid_size)
        # self.maze.edges_count()
    def draw(self, cell) -> None:
        blue = pygame.Color("#ADD8E6")
        x, y = cell.row * self.cell_size, cell.col * self.cell_size
        if cell.visited:
            pygame.draw.rect(self.dis, blue, (x, y, self.cell_size, self.cell_size))
        if cell.walls['top']:
            pygame.draw.line(self.dis, pygame.Color('orange'), (x,y), (x + self.cell_size, y), 4)
        if cell.walls['right']:
            pygame.draw.line(self.dis, pygame.Color('orange'), (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 4)
        if cell.walls['bottom']:
            pygame.draw.line(self.dis, pygame.Color('orange'), (x + self.cell_size, y + self.cell_size), (x, y + self.cell_size), 4)
        if cell.walls['left']:
            pygame.draw.line(self.dis, pygame.Color('orange'), (x, y + self.cell_size), (x, y), 4)
    def draw_current_cell(self, cell) -> None:
        x, y = cell.row * self.cell_size, cell.col * self.cell_size
        pygame.draw.rect(self.dis, pygame.Color('brown'), (x, y, self.cell_size - 2, self.cell_size - 2))
    def remove_walls(self, current, next) -> None:
        x_distance = current.row - next.row
        if x_distance == 1:
            current.walls['left'] = False
            next.walls['right'] = False
        elif x_distance == -1:
            current.walls['right'] = False
            next.walls['left'] = False
        y_distance = current.col - next.col
        if y_distance == 1:
            current.walls['top'] = False
            next.walls['bottom'] = False
        elif y_distance == -1:
            current.walls['bottom'] = False
            next.walls['top'] = False
    def get_graph(self):
        return self.maze.graph
    def get_grid(self):
        return self.maze.grid

#Main for running Maze Generator and Solver
if __name__=="__main__":
    maze = Maze()
    graph = maze.get_graph()
    current_cell = list(graph.keys())[0]
    stack = []
    count = 1

    kruskals_maze = []
    for cell in graph:
        for neighbor in graph[cell]:
            kruskals_maze.append(neighbor)
    kruskals_maze = sorted(kruskals_maze, key=lambda item: item[1])
    
    for cell in kruskals_maze:
        cell[0].print_cell()
        print("weight = %d" % cell[1])

    #Main game loop
    exit = False
    clock = pygame.time.Clock()
    while not exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit = True
        [maze.draw(cell) for cell in maze.get_grid()]

        #Iterative backtracking of DFS
        if count != len(maze.get_grid()):
            current_cell.visited = True
            maze.draw_current_cell(current_cell)
            next_cell = current_cell.check_neighbors()
            if next_cell:
                stack.append(current_cell)
                count += 1
                maze.remove_walls(current_cell, next_cell)
                next_cell.visited = True
                current_cell = next_cell
            elif stack:
                current_cell = stack.pop()
        pygame.display.flip()
        clock.tick(10)
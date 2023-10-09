import pygame
import random
from grid import Grid

def depth_first_search(maze):
    graph = maze.get_graph()
    start_cell = list(graph.keys())[0]
    stack = set()
    traversal = dfs(stack, graph, start_cell, maze)
    for cell in traversal:
        cell.print_cell()
def dfs(stack, graph, cell, maze):
    maze.draw_current_cell(cell)
    if not cell.visited:
        stack.add(cell)
        cell.visited = True
        for neighbor in graph[cell]:
            dfs(stack, graph, neighbor, maze)
    return stack

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
    def draw(self, cell):
        x, y = cell.row * self.cell_size, cell.col * self.cell_size
        if cell.visited:
            pygame.draw.rect(self.dis, pygame.Color('midnightblue'), (x, y, self.cell_size, self.cell_size))
            
        if cell.walls['top']:
            pygame.draw.line(self.dis, pygame.Color('purple4'), (x,y), (x + self.cell_size, y), 4)
        if cell.walls['right']:
            pygame.draw.line(self.dis, pygame.Color('purple4'), (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 4)
        if cell.walls['bottom']:
            pygame.draw.line(self.dis, pygame.Color('purple4'), (x + self.cell_size, y + self.cell_size), (x, y + self.cell_size), 4)
        if cell.walls['left']:
            pygame.draw.line(self.dis, pygame.Color('purple4'), (x, y + self.cell_size), (x, y), 4)
    def draw_current_cell(self, cell):
        x, y = cell.row * self.cell_size, cell.col * self.cell_size
        pygame.draw.rect(self.dis, pygame.Color('brown'), (x + 2, y + 2, self.cell_size - 2, self.cell_size - 2))
    def remove_walls(self, current, next):
        pass
    def get_graph(self):
        return self.maze.graph
    def get_grid(self):
        return self.maze.grid

#Main for running Maze Generator and Solver
if __name__=="__main__":
    maze = Maze()
    graph = maze.get_graph()
    start_cell = list(graph.keys())[0]
    stack = []
    stack.append(start_cell)
    next_cell = -1
    
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
        #Iterative version of DFS
        if len(stack) > 0:
            # next_cell = random.randint(0, len(stack) - 1)
            current_cell = stack.pop(next_cell)
            if not current_cell.visited:
                current_cell.visited = True
                maze.draw_current_cell(current_cell)
                for neighbor in graph[current_cell]:
                    if not neighbor.visited:
                        stack.append(neighbor)
        pygame.display.flip()
        clock.tick(5)
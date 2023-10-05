import pygame
from grid import Grid

def dfs(stack, maze, cell):
    if not cell.visited:
        stack.add(cell)
        cell.visited = True
        for neighbor in maze[cell]:
            dfs(stack, maze, neighbor)
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
    def draw(self):
        for cell in self.maze.grid:
            x, y = cell.row * self.cell_size, cell.col * self.cell_size
            if cell.visited:
                pygame.draw.rect(self.dis, pygame.Color('midnightblue'), (x, y, self.cell_size, self.cell_size))
            
            if cell.walls['top']:
                pygame.draw.line(self.dis, pygame.Color('purple4'), (x,y), (x + self.cell_size, y), 2)
            if cell.walls['right']:
                pygame.draw.line(self.dis, pygame.Color('purple4'), (x + self.cell_size, y), (x + self.cell_size, y + self.cell_size), 2)
            if cell.walls['bottom']:
                pygame.draw.line(self.dis, pygame.Color('purple4'), (x + self.cell_size, y + self.cell_size), (x, y + self.cell_size), 2)
            if cell.walls['left']:
                pygame.draw.line(self.dis, pygame.Color('purple4'), (x, y + self.cell_size), (x, y), 2)
        
    def run(self):
        self.exit = False
        self.clock = pygame.time.Clock()
        while not self.exit:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.exit = True
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.exit = True
            self.draw()
            pygame.display.flip()
            self.clock.tick(30)


#Main for running Maze Generator and Solver
if __name__=="__main__":
    maze = Grid(3,3)
    maze2 = Maze()
    maze2.run()

    print("Grid: ")
    maze.print_grid()
    print("Graph: ")
    maze.print_graph()

    #Testing DFS on current framework:
    graph = maze.get_graph()
    start = list(graph.keys())[0]
    stack = set()
    traversal = dfs(stack, graph, start)
    for cell in traversal:
        cell.print_cell()
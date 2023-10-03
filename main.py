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
    def __init__(self, grid_size) -> None:
        pygame.init()
        self.DIS_WIDTH = grid_size
        self.DIS_HEIGHT = grid_size
        self.dis = pygame.display.set_mode((self.DIS_WIDTH, self.DIS_HEIGHT))
        pygame.display.set_caption("Maze")
        self.maze = Grid(grid_size, grid_size)
        self.maze.draw()
    def draw_maze(self):
        pass

#Main for running Maze Generator and Solver
if __name__=="__main__":
    maze = Grid(3,3)
    maze2 = Maze(3)

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
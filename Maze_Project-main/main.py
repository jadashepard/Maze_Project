import pygame
import random
from grid import Grid
from gui import names2
from gui import names3

#Helper class to create Edge object for Kruskal's algorithm
class Edge:
    def __init__(self, source, dest) -> None:
        self.source = source
        self.dest = dest
        self.weight = random.randint(1, 1000)
class KruskalMST:
    def __init__(self, grid) -> None:
        #Initializing Kruskal's Algorithm for Maze generation
        self.edges_list = []
        self.parent_list = []
        self.numCells = 0
        cell_id = 0

        for cell in grid:
            cell.cell_id = cell_id
            self.numCells += 1
            cell_id += 1
            #Check if sorting function is correct
            for neighbor in cell.neighbors:
                edge = Edge(cell, neighbor)
                self.edges_list.append(edge)

        #Sort the list of edges in ascending order by weight
        self.edges_list = sorted(self.edges_list, key=lambda item: item.weight)
        
        #Initialize parent_list
        i = 0
        while (i < self.numCells):
            self.parent_list.append(i)
            i += 1
    def quickFind(self, id: int):
        if(self.parent_list[id] == id):
            return id
        return self.quickFind(self.parent_list[id])
    def quickUnion(self, source_id, dest_id):
        self.parent_list[source_id] = dest_id

class Maze:
    def __init__(self) -> None:
        pygame.init()
        pygame.display.set_caption("Maze")
        self.RES = 600
        self.dis = pygame.display.set_mode((self.RES + 20, self.RES + 20))
        self.dis.fill('ivory')
        self.grid_size = 10
        self.cell_size = self.RES / self.grid_size
        # assign grid size to value selected by user in gui
        self.grid_size = int(names2[0])
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
    def get_grid(self):
        return self.maze.grid

#Main for running Maze Generator and Solver
if __name__=="__main__":
    maze = Maze()
    grid = maze.get_grid()

    #Kruskal's alorithm functions using edges. All edges in the grid are added to the list
    #and sorted in ascending order by their weights
    kruskal = KruskalMST(grid)
    kruskal_edges = kruskal.edges_list


    DFS = False
    if names3.__contains__('DFS'):
        DFS = True
    current_cell = grid[0]
    stack = []
    count = 0
    i = 0

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
        [maze.draw(cell) for cell in grid]

        if DFS:
            #Iterative backtracking of DFS
            if count != len(grid):
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
        else:
            #Kruskal's Algorithm
            if count != (len(grid) - 1):
                edge = kruskal_edges[i]
                current_cell = edge.source
                current_cell.visited = True
                maze.draw_current_cell(current_cell)
                next_cell = edge.dest
                source_id = kruskal.quickFind(current_cell.cell_id)
                dest_id = kruskal.quickFind(next_cell.cell_id)
                
                #If the parent/root of the current cell and the next cell are not the same, add this edge
                if source_id != dest_id:
                    stack.append(current_cell)
                    maze.remove_walls(current_cell, next_cell)
                    next_cell.visited = True
                    kruskal.quickUnion(source_id, dest_id)
                    count += 1
                i += 1
        pygame.display.flip()
        clock.tick(10)
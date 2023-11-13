import random
class Cell:
    def __init__(self, row: int, col: int):
        self.row, self.col = row, col
        self.cell_id = 0
        self.walls = {'top': True, 'right': True, 'bottom': True, 'left': True}
        self.neighbors = []
        self.visited = False
    def check_neighbors(self):
        unvisited = []
        for neighbor in self.neighbors:
            if not neighbor.visited:
                unvisited.append(neighbor)
        return unvisited[random.randint(0, len(unvisited) - 1)] if unvisited else False
    def print_cell(self):
        cell_string = str(self.row) + ',' + str(self.col)
        return cell_string

class Grid:
    def __init__(self, num_rows: int, num_cols: int):
        self.rows = num_rows
        self.cols = num_cols
        self.grid = [Cell(col,row) for row in range(self.rows) for col in range(self.cols)]
        self.configure_cells()
        self.graph = self.create_graph()

    def create_graph(self):
        graph = {cell: cell.neighbors for cell in self.grid}
        return graph

    def configure_cells(self):
        #For each cell in the grid:
        #Find the index of the neighboring cells and add them to the cell's list of neighbors
        for cell in self.grid:
            left = self.check_cell(cell.row, cell.col - 1)
            bottom = self.check_cell(cell.row + 1, cell.col)
            right = self.check_cell(cell.row, cell.col + 1)
            top = self.check_cell(cell.row - 1, cell.col)
            #If the cell is a top, right, bottom, or left neighbor it added to the list as a tuple
            #with the first index being the cell and the second index being a random integer to act as the weight of the edge
            #tuple (Cell, weight:int)
            if top:
                cell.neighbors.append(top)
            if right:
                cell.neighbors.append(right)
            if bottom:
                cell.neighbors.append(bottom)
            if left:
                cell.neighbors.append(left)
    #Helper method for algorithm analysis
    def edges_count(self):
        vertices = 0
        edges = 0
        for cell in self.graph:
            vertices += 1
            edges += len(self.graph[cell])
        print("Number of vertices: " + str(vertices))
        print("Number of edges: " + str(edges))

    #Goal: check_cell returns if the cell we are looking for is our neighbor. 
    #Find index of neighboring cells in 1D list = Cell.row + Cell.col * total number of columns
    def check_cell(self, row: int, col: int):
        find_index = lambda row, col: row + col * self.cols
        #If the row or column is outside the boundary of the grid, it is not a neighboring cell
        if(row < 0 or row > self.rows - 1 or col < 0 or col > self.cols - 1):
            return False
        #Else, return the neighboring cell which is at the index calculated by the lambda function
        return self.grid[find_index(row,col)]
    def print_graph(self):
        for key in self.graph:
            print()
            key.print_cell()
            print("__")
            for value in self.graph[key]:
                value.print_cell()
        print(self.graph.items())
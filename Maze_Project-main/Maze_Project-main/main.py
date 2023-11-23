from grid import Grid
from gui import names2

def dfs(stack, maze, cell):
    if not cell.visited:
        stack.add(cell)
        cell.visited = True
        for neighbor in maze[cell]:
            dfs(stack, maze, neighbor)
    return stack

#Main for running Maze Generator and Solver
if __name__=="__main__":

    maze = Grid(int(names2[0]),(int(names2[0])))

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
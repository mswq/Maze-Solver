import random
from dfs import *
from bfs import *

class MazeGenerator(StackFrontier):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height
        self.visited = []
        self.frontier = []
        self.start = None
        self.final_goal = None
        
        self.grid = []
        for x in range(self.height):
            row = []
            for y in range(self.width):
                row.append('#')
            self.grid.append(row)
    
    def replace_wall(self, x, y, value):
        self.grid[x][y] = value
 
    def neighbors(self, node):
        neighbors = []
        row, col = node.state
        directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
        for x, y in directions:
            r, c = row + x, col + y
            if 0 <= r <= self.height - 1 and 0 <= c <= self.width - 1:
                if self.grid[r][c] == "#":
                    neighbors.append(Node((r, c), node))
        return neighbors
    
    def goal(self):
        while True:
            goal = random.choice(self.visited)
            if goal != self.start.state:
                x, y = goal
                self.replace_wall(x, y, "B")
                break
    
    def run(self):
        self.start = Node((random.randint(0, self.height- 1), random.randint(0, self.width - 1)), None)
        self.visited.append(self.start.state)
        x, y = self.start.state
        self.replace_wall(x, y, "A")
        self.add(self.start)

        while not self.is_empty():
            current = self.top()
            x, y = current.state
            neighbors = self.neighbors(current)
            unvisited = [n for n in neighbors if n.state not in self.visited]
            if unvisited:
                neighbor = random.choice(unvisited)
                m, n = neighbor.state
                wall_row = (x + m) //2
                wall_col = (y + n) //2
                self.replace_wall(m, n, " ")
                self.replace_wall(wall_row, wall_col, " ")
                self.visited.append(neighbor.state)
                self.add(neighbor)
            else: 
                self.remove()   
        self.final_goal = self.goal()

    def to_solve(self):
        file_path = "m.txt"
        with open(file_path, 'w') as file:
            for i in range(self.height):
                for j in range(self.width):
                    file.write(self.grid[i][j])
                file.write("\n")
        return file_path
        
    def print(self):
        for i, row in enumerate(self.grid):
            for j, value in enumerate(row):
                if value == "#":
                    print ("⬜", end='')
                elif value == "A":
                    print("🟥", end='')
                    self.start = Node((i, j), None)
                elif value == "B":
                    print("🟩", end='')
                    self.goal = (i,j)
                elif value == " ":
                    print("⬛", end='')
            print("\n")
                
    def start_node(self):
        return self.start

'''
Start with a grid FULL of walls.

Pick a starting cell and mark it as a passage.

From the current cell, pick a neighbor two steps away (to skip over a wall).

If the neighbor is unvisited, knock down the wall between the current and the neighbor.

Mark the neighbor as passage, push it to the stack.

If no neighbors, backtrack.
'''

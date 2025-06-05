class Node():
    def __init__(self, state, parent):
        self.state = state
        self.parent = parent
        # self.action = action

class QueueFrontier(): 
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)
    
    def contains_state(self, state):
        for node in self.frontier:
            if node.state == state:
                return node
    
    def is_empty(self):
        if len(self.frontier) == 0:
            return True
        return False

    def remove(self):
        if self.is_empty():
            raise Exception("frontier is empty")   
        return self.frontier.pop(0)

class Maze():
    def __init__(self, filename):
        self.solution = []
        with open(filename) as f:
            contents = f.read()
            self.contents = contents.splitlines()
            self.height = len(self.contents)
            self.width = max(len(line) for line in self.contents)
            print (self.contents)
            print("height", self.height)
            print ("width", self.width)

    def print(self):
        for i, row in enumerate(self.contents):
            for j, value in enumerate(row):
                if value == "#":
                    print ("⬜", end='')
                elif value == "A":
                    print("🟥", end='')
                    self.start = Node((i, j), None)
                elif value == "B":
                    print("🟩", end='')
                elif value == " ":
                    print("⬛", end='')
                    self.goal = (i,j)
            print("\n")

    def neighbors(self, node):
        neighbors = []
        row, col = node.state

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in directions:
            r, c = row + x, col + y
            if 0 <= r <= self.height and 0 <= c <= self.width:
                if self.contents[r][c] == " ":
                    neighbors.append((r, c))
        return neighbors

    def maze_solution(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        self.solution = list(reversed(path))
        
    def print_solution(self):
        for node in self.solution:
            for i, row in enumerate(self.contents):
                for j, value in enumerate(row):
                    if value == "#":
                        print ("⬜", end='')
                    elif value == "A":
                        print("🟥", end='')
                        self.start = Node((i, j), None)
                    elif value == "B":
                        print("🟩", end='')
                    elif value == " ":
                        is_sol = False
                        for node in self.solution: 
                            if (i, j) == node.state:
                                print("🟦", end='')
                                is_sol = True
                                break
                        if not is_sol:
                            print("⬛", end='')
                    
                print("\n")


if __name__ == "__main__":
    maze = Maze("maze1.txt")
    frontier = QueueFrontier()
    maze.print()

    maze_explored = []

    # Add initial start 
    start = maze.start
    frontier.add(start)
    maze_explored.append(start.state)

    while True:
        # If frontier is empty -> no solution
        if frontier.is_empty():
            print("\nNo Solution")
            break

        # Remove a node from the frontier
        node = frontier.remove()
        # Add the node to the explored set
        maze_explored.append(node.state)

        # If node contains a goal state -> return the solution
        if node.state == maze.goal:
            maze.maze_solution(node)
            maze.print_solution()
            break

        # Take the next step
        neighbors = maze.neighbors(node)

        for neighbor in neighbors:
            if not frontier.contains_state(neighbor) and neighbor not in maze_explored:
                to_add = Node(neighbor, parent=node)
                print("\n added", to_add.state)
                frontier.add(to_add)

            

  
    
   
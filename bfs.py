
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
                    self.goal = (i,j)
                elif value == " ":
                    print("⬛", end='')
            print("\n")

    def neighbors(self, node):
        neighbors = []
        row, col = node.state
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for x, y in directions:
            r, c = row + x, col + y
            if 0 <= r <= self.height - 1 and 0 <= c <= self.width - 1:
                if self.contents[r][c] == " " or self.contents[r][c] == "B":
                    neighbors.append((r, c))
        return neighbors

    def maze_solution(self, node):
        path = []
        while node is not None:
            path.append(node)
            node = node.parent
        self.solution = list(reversed(path))
        
    def print_solution(self):
        print ("Solution")
        for i, row in enumerate(self.contents):
            for j, value in enumerate(row):
                if value == "#":
                    print ("⬜", end='')
                elif value == "A":
                    print("🟥", end='')
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



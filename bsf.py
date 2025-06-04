class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier(): 
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
        del self.frontier[0]
    
class Maze():
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

            self.contents = contents.splitlines()
            self.height = len(self.contents)
            self.width = max(len(line) for line in self.contents)

    def print(self):
        for row in self.contents:
            for i, value in enumerate(row):
                if value == "#":
                    print ("⬜", end='')
                elif value == "A":
                    print("🟥", end='')
                elif value == "B":
                    print("🟩", end='')
                elif value == " ":
                    print("⬛", end='')
            print("\n")

if __name__ == "__main__":
    maze = Maze("maze1.txt")
    maze.print()

   
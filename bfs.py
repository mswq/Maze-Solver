import time
import os
from PIL import Image, ImageDraw
import imageio

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

    def explore_path(self, explore):
        print ("\nFinding Solution...")
        for length in range(len(explore)):
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
                        for node in explore[:length]: 
                            if (i, j) == node:
                                print ("🟨", end='')
                                is_sol = True
                                break
                        if not is_sol:
                            print("⬛", end='')
                print()
            time.sleep(0.2)
        return len(explore)
    
    import os

    def save_exploration_gif(self, explore, gif_name='maze_exploration.gif'):
        cell_size = 20  # pixels per maze cell
        maze_height = self.height
        maze_width = self.width

        image_width = maze_width * cell_size
        image_height = maze_height * cell_size

        frames = []

        for length in range(1, len(explore) + 1):
            # Create a blank white image
            img = Image.new('RGB', (image_width, image_height), color='white')
            draw = ImageDraw.Draw(img)

            for i in range(maze_height):
                for j in range(maze_width):
                    x0 = j * cell_size
                    y0 = i * cell_size
                    x1 = x0 + cell_size
                    y1 = y0 + cell_size

                    value = self.contents[i][j]

                    if value == "#":
                        color = (0, 0, 0)  # black wall
                    elif value == "A":
                        color = (255, 0, 0)  # red start
                    elif value == "B":
                        color = (0, 255, 0)  # green goal
                    elif value == " ":
                        if (i, j) in explore[:length]:
                            color = (250, 156, 28)  # orange explored
                        else:
                            color = (255, 255, 255)  # white passage

                    draw.rectangle([x0, y0, x1, y1], fill=color, outline=(200, 200, 200))

            frames.append(img)

        for _ in range(10):  # Repeat to hold on solution for a while
            img = Image.new('RGB', (image_width, image_height), color='white')
            draw = ImageDraw.Draw(img)

            for i in range(maze_height):
                for j in range(maze_width):
                    x0 = j * cell_size
                    y0 = i * cell_size
                    x1 = x0 + cell_size
                    y1 = y0 + cell_size

                    value = self.contents[i][j]

                    if value == "#":
                        color = (0, 0, 0)  # wall
                    elif value == "A":
                        color = (255, 0, 0)  # start
                    elif value == "B":
                        color = (0, 255, 0)  # goal
                    elif value == " ":
                        # If in solution path, make blue
                        if any(node.state == (i, j) for node in self.solution):
                            color = (26, 163, 255)  # blue solution
                        else:
                            color = (255, 255, 255)  # passage

                    draw.rectangle([x0, y0, x1, y1], fill=color, outline=(200, 200, 200))

            frames.append(img)

        # Save frames as GIF
        frames[0].save(
            gif_name,
            save_all=True,
            append_images=frames[1:],
            duration=200,  # ms per frame
            loop=0
        )

        print(f"GIF saved as {gif_name}")


        
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
                            print ("🟦", end='')
                            is_sol = True
                            break
                    if not is_sol:
                        print("⬛", end='')
            print()




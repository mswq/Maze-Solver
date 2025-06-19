from bfs import *
from dfs import *
from main_generator import *

if __name__ == "__main__":

    #maze = Maze("m.txt")
    frontier = StackFrontier()

    gen_maze = MazeGenerator(21, 11)
    gen_maze.run()

    print("Maze:")

    maze = gen_maze.to_solve()
    maze = Maze(maze)
    maze.print()

    maze_explored = []

    # Add initial start 
    start = maze.start
    frontier.add(start)

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
            node_amt = maze.explore_path(maze_explored)
            maze.print_solution()
            print (f"\nNodes Visited: {node_amt}")
            maze.save_exploration_gif(maze_explored, "dfs.gif")
            break

        # Take the next step
        neighbors = maze.neighbors(node)
        for neighbor in neighbors:
            if not frontier.contains_state(neighbor) and neighbor not in maze_explored:
                to_add = Node(neighbor, parent=node)
                frontier.add(to_add)

            

  
    
   
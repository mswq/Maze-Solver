# Maze Generator & Solver with Step-by-Step Animation
This Python project generates a random maze using a randomized depth-first search (DFS) algorithm and solves it using breadth-first search (BFS) or depth-first search (DFS). It visualizes:
- The maze structure
- The step-by-step exploration of nodes
- The final solution path directly in your terminal and exports a clean animated GIF to share or embed.

# How It Works
1. Maze Generation
  a) Starts with a grid full of walls.
  b) Uses randomized DFS to carve passages by knocking down walls between cells.
  c) Randomly places a Start (🟥) and Goal (🟩).

2. Maze Solving
  a) Uses BFS or DFS to find the shortest path from start to goal.
  b) Marks the solution path.

3️.  Visualization
- Terminal: Emoji-based live output.
- GIF: Exports an animated GIF showing:
  - Explored nodes (🟨)
  - Final solution path (🟦)
  
# Example: BFS and DFS Maze Solving with Step-by-Step Visualization
- ⬜ = Wall
- ⬛ = Passage
- 🟥 = Start
- 🟩 = Goal
- 🟨 = Explored node
- 🟦 = Final solution path

<div align="center">
  <table>
    <tr>
      <th align="center">BFS</th>
      <th align="center">DFS</th>
    </tr>
    <tr>
      <td align="center">
        <img src="https://github.com/mswq/Maze-Solver/blob/main/bfs.gif" width="90%">
      </td>
      <td align="center">
        <img src="https://github.com/mswq/Maze-Solver/blob/main/dfs.gif" width="90%">
      </td>
    </tr>
  </table>
</div>


# Key Classes
| Class           | Purpose                                             |
| --------------- | --------------------------------------------------- |
| `Node`          | Represents a maze cell & its parent                 |
| `QueueFrontier` | BFS frontier (FIFO queue)                           |
| `StackFrontier` | DFS frontier (LIFO stack for generation)            |
| `Maze`          | Loads maze, finds neighbors, solves, and visualizes |
| `MazeGenerator` | Creates a random maze with DFS                      |


Maze Solving: Breadth-First Search (guarantees shortest path)




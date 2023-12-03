from queue import Queue
import API
import sys
from Mouse import Mouse
from Direction import Direction
from Maze import Maze
class Micromouse:
    def __init__(self):
        self.maze = []
        self.visited = set()
        self.queue = Queue()
        self.start_position = None
        self.end_position = None

    def is_valid_move(self, x, y):
        return 0 <= x < len(self.maze) and 0 <= y < len(self.maze[0]) and self.maze[x][y] == 0 and (x, y) not in self.visited

    def find_start_end_positions(self):
        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if self.maze[i][j] == (0, 0):
                    self.start_position = (i, j)
                elif self.maze[i][j] == maze.inCenter(mouse.getPosition()):
                    self.end_position = (i, j)
        if self.start_position is None or self.end_position is None:
            raise ValueError("Start or end position not found.")

    def solve_maze(self):
        self.find_start_end_positions()
        if self.start_position is None or self.end_position is None:
            print("Start or end position not found.")
            return

        self.queue.put(self.start_position)
        self.visited.add(self.start_position)

        while not self.queue.empty():
            current_node = self.queue.get()

            if current_node == self.end_position:
                print("Maze solved!")
                return

            x, y = current_node

            # Check and enqueue valid neighbors
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for neighbor in neighbors:
                nx, ny = neighbor
                if self.is_valid_move(nx, ny):
                    self.queue.put(neighbor)
                    self.visited.add(neighbor)

    def print_solution(self):
        self.solve_maze()
        path = list(self.visited)

        for i in range(len(self.maze)):
            for j in range(len(self.maze[0])):
                if (i, j) == self.start_position:
                    print("S", end=" ")
                elif (i, j) == self.end_position:
                    print("E", end=" ")
                elif (i, j) in path:
                    print(".", end=" ")
                else:
                    print("#", end=" ")
            print()

    def add_row(self, row):
        self.maze.append(row)

    def log(string):
        sys.stderr.write("{}\n".format(string))
        sys.stderr.flush()


if __name__ == "__main__":
    micromouse = Micromouse()
    mouse = Mouse(0, 0, Direction.NORTH)
    maze = Maze(API.mazeWidth(), API.mazeHeight())
    # Example: Add rows to the maze dynamically
    micromouse.add_row(['S', 0, 0, 0, 0])
    micromouse.add_row([0, 0, 0, 1, 'E'])
    micromouse.add_row([1, 1, 0, 1, 0])
    micromouse.add_row([0, 0, 0, 0, 0])
    micromouse.add_row([0, 1, 1, 1, 1])
    

    micromouse.print_solution()
    a =API.mazeWidth()
    micromouse.log(a)
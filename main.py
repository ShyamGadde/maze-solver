import random
from queue import Queue

START = "\033[92mS\033[0m"
END = "\033[92mE\033[0m"
WALL = "\033[91m▓\033[0m"
OPEN_SPACE = "\033[94m◌\033[0m"
PATH = "\033[92m◍\033[0m"
ROW_SEPARATOR = "\033[91m---+\033[0m"
COLUMN_SEPARATOR = "|"


def generate_maze(size, wall_percentage):
    maze = [
        [
            WALL if random.randint(1, 100) <= wall_percentage else OPEN_SPACE
            for _ in range(size)
        ]
        for _ in range(size)
    ]
    maze[0][0] = START
    maze[size - 1][size - 1] = END
    return maze


def print_maze(maze):
    separator = ROW_SEPARATOR
    for i, row in enumerate(maze):
        print(f"{COLUMN_SEPARATOR}{COLUMN_SEPARATOR.join(row)}{COLUMN_SEPARATOR}")
        if i < len(maze) - 1:
            print(separator * (len(row) // 2))


def find_path(maze, start, end):
    queue = Queue()
    queue.put(start)
    parent = {start: None}

    while not queue.empty():
        current = queue.get()
        if current == end:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            path.reverse()
            return path

        row, col = current
        neighbors = [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]
        for neighbor in neighbors:
            n_row, n_col = neighbor
            if (
                0 <= n_row < len(maze)
                and 0 <= n_col < len(maze[0])
                and maze[n_row][n_col] != WALL
                and neighbor not in parent
            ):
                queue.put(neighbor)
                parent[neighbor] = current

    return None


def print_path(maze, path):
    for row, col in path[1:-1]:
        maze[row][col] = PATH
    print_maze(maze)


def ratinmaze():
    size = int(input("Enter the size of the maze: "))
    wall_percentage = int(input("Enter the percentage of walls in the maze: "))

    while True:
        maze = generate_maze(size, wall_percentage)
        print("Generated Maze:")
        print_maze(maze)

        start = (0, 0)
        end = (size - 1, size - 1)

        path = find_path(maze, start, end)

        if path:
            print("Path Found:")
            print_path(maze, path)
        else:
            print("No path found from start to end.")

        option = int(
            input("Options: Print Path (1), Generate Another Puzzle (2), Exit (3)\n")
        )
        if option == 1:
            print("Path:")
            print_path(maze, path)
        elif option == 2:
            continue
        elif option == 3:
            break
        else:
            print("Invalid option. Exiting.")
            break


if __name__ == "__main__":
    ratinmaze()

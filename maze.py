# maze.py
import random

# Дефолтные настройки
ROWS = 11
COLS = 11
WALL = '#'
PATH = ' '
VISITED = '.'
START = 'S'
END = 'E'
def create_empty_maze():
    return [[WALL for _ in range(COLS)] for _ in range(ROWS)]
def is_valid(r, c):
    return 0 <= r < ROWS and 0 <= c < COLS
def generate_maze(maze, r, c):
    directions = [(-2, 0), (2, 0), (0, -2), (0, 2)]
    random.shuffle(directions)
    
    maze[r][c] = PATH
    
    for dr, dc in directions:
        nr, nc = r + dr, c + dc
        if is_valid(nr, nc) and maze[nr][nc] == WALL:
            maze[r + dr//2][c + dc//2] = PATH
            generate_maze(maze, nr, nc)
            def set_start_end(maze):
                maze[0][0] = START
                maze[-1][-1] = END 
    def find_path(maze, r, c):
        if not is_valid(r, c) or maze[r][c] in (WALL, VISITED):
            return False
        
        if maze[r][c] == END:
             return True
        
    if maze[r][c] != START:
        maze[r][c] = VISITED
        
    # Проверяем все направления
    if find_path(maze, r+1, c) or find_path(maze, r-1, c) or find_path(maze, r, c+1) or find_path(maze, r, c-1):
        return True
        
    # Откат
    if maze[r][c] != START:
        maze[r][c] = PATH
    return False
def print_maze(maze):
    for row in maze:
        print(' '.join(row))
def validate_size(rows, cols):
    if rows % 2 == 0 or cols % 2 == 0:
        raise ValueError("Размеры должны быть нечетными!")
    if __name__ == "__main__":
        try:
            validate_size(ROWS, COLS)
            maze = create_empty_maze()
            generate_maze(maze, 0, 0)
            set_start_end(maze) 

            if find_path(maze, 0, 0):
                print("Путь найден!")
            else:
                print("Путь не найден!")

                print_maze(maze)
        except ValueError as e:
                print(f"Ошибка: {e}")


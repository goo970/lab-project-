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
s
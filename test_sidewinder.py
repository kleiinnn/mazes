from sidewinder import sidewinder
from grid import Grid

grid = Grid(10, 10)
sidewinder(grid)
print(grid)

grid.to_svg(100).write(open('maze.svg', 'w', encoding='utf-8'))

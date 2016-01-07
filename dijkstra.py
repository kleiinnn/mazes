import grid_utils

from grid import Grid
from binary_tree import binary_tree

grid = Grid(5, 5)
binary_tree(grid)

print(grid_utils.to_ascii(grid,
      cell_body=grid_utils.distance_cell_body(grid[0, 0])))

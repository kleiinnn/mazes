from binary_tree import binary_tree
from grid import Grid
from graph_grid import GraphGrid
import grid_utils

grid = Grid(10, 10)
binary_tree(grid)

print(grid.to_ascii(cell_body=grid_))

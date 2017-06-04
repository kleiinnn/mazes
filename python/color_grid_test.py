from sidewinder import sidewinder
from binary_tree import binary_tree
from grid import Grid
from graph_grid import GraphGrid

grid = Grid(10, 10)
sidewinder(grid)

distances = grid[4, 4].distances()
dwg = grid.to_colored_svg(50, distances.cell_color, with_borders=False)
dwg.saveas('foobar.svg')

import grid_utils

from grid import Grid
from binary_tree import binary_tree
from sidewinder import sidewinder

grid = Grid(5, 5)
sidewinder(grid)

distances = grid[0, 0].distances()
new_start, distance = distances.max()

new_distances = new_start.distances()
goal, distance = new_distances.max()

print(grid_utils.to_ascii(grid,
      cell_body=grid_utils.distance_cell_body(distances)))

print(grid_utils.to_ascii(
    grid,
    cell_body=grid_utils.distance_cell_body(
        new_distances.path_to(goal)
    )
))

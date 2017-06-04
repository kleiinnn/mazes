import random

def binary_tree(grid):
    for cell in grid:
        neighbors = []
        if cell.north: neighbors.append(cell.north)
        if cell.east: neighbors.append(cell.east)

        try:
            cell.link(random.choice(neighbors))
        except IndexError:
            pass

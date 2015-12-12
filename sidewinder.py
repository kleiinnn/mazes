import random

def sidewinder(grid):
    for row in grid.each_rows():
        start, end = 0, 0

        for index, cell in enumerate(row):
            end = index + 1

            if not cell.north and not cell.east:
                pass
            elif cell.east is not None and random.randrange(2) == 1 or cell.north is None:
                cell.link(cell.east)
            else:
                link_cell = random.choice(row[start:end])
                link_cell.link(link_cell.north)

                start = end

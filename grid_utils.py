
def to_ascii(grid, cell_body = None):
    output = '+' + ('---+' * grid.columns) + '\n'

    for row in grid.each_rows():
        top = '|'
        bottom = '+'

        for cell in row:
            if not cell: cell = Cell(-1, -1)

            body = cell_body(cell) if cell_body is not None else '   '

            top += body + (' ' if cell.is_linked(cell.east) else '|')
            bottom += ('   ' if cell.is_linked(cell.south) else '---') + '+'

        output += top + '\n'
        output += bottom + '\n'

    return output

def to_svg(grid):
    dwg = svgwrite.Drawing(width=cell_size * grid.columns,
                           height=cell_size * grid.rows)

    for cell in grid:
        north_west = (cell.column * cell_size, cell.row * cell_size,)
        south_east = ((cell.column + 1) * cell_size, (cell.row + 1) * cell_size,)

        if not cell.north:
            dwg.add(dwg.line(north_west, (south_east[0], north_west[1]), stroke='#000000'))
        if not cell.west:
            dwg.add(dwg.line(north_west, (north_west[0], south_east[1]), stroke='#000000'))

        if not cell.is_linked(cell.east):
            dwg.add(dwg.line((south_east[0], north_west[1]), south_east, stroke='#000000'))
        if not cell.is_linked(cell.south):
            dwg.add(dwg.line((north_west[0], south_east[1]), south_east, stroke='#000000'))

    return dwg

def distance_cell_body(start):
    distances = start.distances()
    return lambda cell: '{:^3}'.format(distances[cell])

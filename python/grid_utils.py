def distance_cell_body(distances):
    def format_body(cell):
        if distances[cell] is None:
            return '   '
        else:
            return '{:^3}'.format(distances[cell])

    return format_body

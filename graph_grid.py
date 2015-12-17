from grid import Cell

class GraphGrid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.north_east = None
        self._init_grid()

    def __getitem__(self, index):
        row, column = index

        if row not in range(0, self.rows) or column not in range(0, self.columns):
            return None

        cell = self.north_east

        for ctr in range(row):
            cell = cell.south

        for ctr in range(column):
            cell = cell.east

        return cell

    def __len__(self):
        return self.rows * self.columns

    def __iter__(self):
        row = self.north_east

        while row.south:
            cell = row
            while cell.east:
                yield cell
                cell = cell.east

            row = row.south

    def __repr__(self):
        '''
        Returns an ascii representation of this grid.
        '''
        output = '+' + ('---+' * self.columns) + '\n'

        for row in self.each_rows():
            top = '|'
            bottom = '+'

            for cell in row:
                if not cell: cell = Cell(-1, -1)

                top += '   ' + (' ' if cell.is_linked(cell.east) else '|')
                bottom += ('   ' if cell.is_linked(cell.south) else '---') + '+'

            output += top + '\n'
            output += bottom + '\n'

        return output

    def each_rows(self):
        def each_row():
            cell = row

            while cell.east:
                yield cell
                cell = cell.east

        row = self.north_east

        while row.south:
            yield each_row()
            row = row.south

    def _init_grid(self):
        self.north_east = Cell(0, 0)
        cell = self.north_east

        row = self.north_east

        last_row = None
        last_row_cell = None

        while row.row < self.rows:
            while cell.column < self.columns:
                new_cell = Cell(row.row, cell.column + 1)

                if last_row_cell:
                    last_row_cell = last_row_cell.east
                    new_cell.north = last_row_cell
                    last_row_cell.south = new_cell




                new_cell.west = cell
                cell.east = new_cell

                cell = new_cell

            last_row = row
            row = Cell(row.row + 1, 0)

            if last_row:
                row.north = last_row
                last_row.south = row

            cell = row
            last_row_cell = last_row

        '''
        last_cell = self.north_east
        last_row_cell = None

        for row in range(self.rows):
            row_start = last_cell
            last_cell = None

            for column in range(1, self.columns):
                new_cell = Cell(row, column)

                if last_row_cell:
                    new_cell.north = last_row_cell
                    last_row_cell.south = new_cell

                if last_cell:
                    new_cell.east = last_cell
                    last_cell.west = last_cell

                last_cell = new_cell
                if last_row_cell and last_row_cell.west:
                    last_row_cell = last_row_cell.west

            last_row_cell = row_start
        '''

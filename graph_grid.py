from grid import Cell
from grid_utils import to_ascii

class RowWrapper:
    def __init__(self, start_cell, grid):
        self.start_cell = start_cell
        self.grid = grid

    def __iter__(self):
        cell = self.start_cell
        while cell.east:
            yield cell
            cell = cell.east

        yield cell

    def __getitem__(self, index):
        if type(index) is not slice:
            index = slice(index, index+1)

        start, stop, step = index.indices(self.grid.columns)

        cell = self.start_cell

        while start > cell.column:
            cell = cell.east

        cells = []
        counter = 0
        while (stop - 1) > cell.column:
            if counter % step == 0:
                cells.append(cell)

            cell = cell.east

            counter = (counter + 1) % step

        if counter % step == 0:
            cells.append(cell)

        return cells


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

            yield cell
            row = row.south

    def __repr__(self):
        '''
        Returns an ascii representation of this grid.
        '''
        return to_ascii(self)

    def each_rows(self):
        row = self.north_east
        while row.south:
            yield RowWrapper(row, self)
            row = row.south

        yield RowWrapper(row, self)

    def _init_grid(self):
        '''
        documentation needed!
        '''
        self.north_east = Cell(0, 0)
        cell = self.north_east

        row = self.north_east

        last_row = None
        last_row_cell = None

        while True:
            while (cell.column + 1) < self.columns:
                new_cell = Cell(row.row, cell.column + 1)

                if last_row_cell:
                    last_row_cell = last_row_cell.east
                    new_cell.north = last_row_cell
                    last_row_cell.south = new_cell

                new_cell.west = cell
                cell.east = new_cell

                cell = new_cell

            if (row.row + 1) < self.rows:
                last_row = row
                row = Cell(row.row + 1, 0)

                if last_row:
                    row.north = last_row
                    last_row.south = row

                cell = row
                last_row_cell = last_row
            else:
                break

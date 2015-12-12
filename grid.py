class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column

        self.__links = []
        self.north = None
        self.east = None
        self.south = None
        self.west = None

    def is_linked(self, cell):
        return cell in self.__links

    def link(self, cell, bidi=True):
        self.__links.append(cell)

        if bidi:
            cell.link(self, False)

    def unlink(self, cell, bidi=True):
        self.__links.remove(cell)

        if bidi: cell.unlink(self, False)

    def neighbors(self):
        neighbors = []

        if self.north: neighbors.append(self.north)
        if self.east: neighbors.append(self.east)
        if self.south: neighbors.append(self.south)
        if self.west: neighbors.append(self.west)


class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns

        self.__grid = self._init_grid()
        self._config_grid()

    def __getitem__(self, index):
        row, column = index

        if row not in range(0, self.rows) or column not in range(0, self.columns):
            return None

        return self.__grid[row][column]

    def __len__(self):
        return self.rows * self.columns

    def __iter__(self):
        for row in self.__grid:
            for cell in row:
                yield cell

    def __repr__(self):
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
        for row in self.__grid:
            yield row


    def _init_grid(self):
        return [[Cell(row, column) for column in range(0, self.columns)]
                for row in range(0, self.rows)]

    def _config_grid(self):
        for cell in self:
            row, col = cell.row, cell.column

            cell.north = self[row - 1, col]
            cell.east  = self[row, col + 1]
            cell.south = self[row + 1, col]
            cell.west  = self[row, col - 1]

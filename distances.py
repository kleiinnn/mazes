class Distances:
    def __init__(self, root):
        self.root = root
        self.cells = {root: 0}

    def __getitem__(self, cell):
        return self.cells.get(cell)

    def __setitem__(self, cell, distance):
        self.cells[cell] = distance

    def __contains__(self, cell):
        return cell in self.cells

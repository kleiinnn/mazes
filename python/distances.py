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

    def path_to(self, goal):
        steps = Distances(self.root)
        steps[goal] = self[goal]

        current = goal
        while current != self.root:
            for neighbor in current.links:
                if self[neighbor] < self[current]:
                    steps[neighbor] = self[neighbor]
                    current = neighbor


        return steps

    def max(self):
        max_distance = 0
        max_dist_cell = self.root

        for cell, distance in self.cells.items():
            if distance > max_distance:
                max_dist_cell = cell
                max_distance = distance

        return (max_dist_cell, max_distance)

    def cell_color(self, cell):
        factor = self.max()[1] - self.cells[cell]
        red = int(255 * factor / self.max()[1])
        green = int(255 * factor / self.max()[1])
        blue = 128 + int(127 * factor / self.max()[1])

        return '#{:02X}{:02X}{:02X}'.format(red, green, blue)

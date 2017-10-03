class HuntAndKill
    def self.on(grid)
        current = grid.random_cell

        while current
            unvisited_neighbors = current.neighbors.select { |n| n.links.empty? }

            if unvisited_neighbors.any?
                neighbor = unvisited_neighbors.sample
                current.link(neighbor)
                current = neighbor
            else
                current = nil

                grid.each_cell do |cell|
                    next if cell.links.any?

                    visited_neighbors = cell.neighbors.select { |n| n.links.any? }
                    if visited_neighbors.any?
                      cell.link(visited_neighbors.sample)
                      current = cell
                      break
                    end
                end
            end
        end
        grid
    end
end

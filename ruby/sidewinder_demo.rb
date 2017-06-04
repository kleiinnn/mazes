require 'grid'
require 'sidewinder'

grid = Grid.new(4, 4)
Sidewinder.on(grid)

puts grid

# Save as PNG
img = grid.to_png cell_size: 50
img.save 'grid.png'

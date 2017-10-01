require 'chunky_png'

require 'cell'

class Grid
    attr_reader :rows, :columns

    def initialize(rows, columns = nil)
        if columns
            @rows, @columns = rows, columns

            @grid = prepare_grid
            configure_cells
        else
            @rows, @columns = rows.size, rows.first.size
            @grid = rows
        end
    end

    def prepare_grid
        Array.new(rows) do |row|
            Array.new(columns) do |column|
                Cell.new(row, column)
            end
        end
    end

    def configure_cells
        each_cell do |cell|
            row, col = cell.row, cell.column

            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]
        end
    end

    def [](row, column = nil)
        return @grid[row] unless column
        return nil unless row.between?(0, @rows - 1)
        return nil unless column.between?(0, @grid[row].count - 1)
        @grid[row][column]
    end

    def random_cell
        @grid.sample.sample
    end

    def size
        @rows * @columns
    end

    def each_row
        @grid.each do |row|
            yield row
        end
    end

    def each_cell
        each_row do |row|
            row.each do |cell|
                yield cell
            end
        end
    end

    def contents_of(cell)
        " "
    end

    def to_s
        output = "+" + "---+" * columns + "\n"

        each_row do |row|
            top = "|"
            bottom = "+"

            row.each do |cell|
                cell = Cell.new(-1, -1) unless cell
                body = " #{contents_of cell} " # <-- that's THREE (3) spaces!
                east_boundary = (cell.linked?(cell.east) ? " " : "|")
                top << body << east_boundary

                # three spaces below, too >>-------------->> >...<
                south_boundary = (cell.linked?(cell.south) ? "   " : "---")
                corner = "+"
                bottom << south_boundary << corner
            end

            output << top << "\n"
            output << bottom << "\n"
        end

        output
    end

    def background_color_for(cell)
        nil
    end

    def to_png(cell_size: 10)
        img_width = cell_size * columns
        img_height = cell_size * rows

        background = ChunkyPNG::Color::WHITE
        wall = ChunkyPNG::Color::BLACK

        img = ChunkyPNG::Image.new(img_width + 1, img_height + 1, background)

        [:backgrounds, :walls].each do |mode|
            each_cell do |cell|
                x1 = cell.column * cell_size
                y1 = cell.row * cell_size
                x2 = (cell.column + 1) * cell_size
                y2 = (cell.row + 1) * cell_size

                if mode == :backgrounds
                    color = background_color_for(cell)
                    img.rect(x1, y1, x2, y2, color, color) if color
                else
                    img.line(x1, y1, x2, y1, wall) unless cell.north
                    img.line(x1, y1, x1, y2, wall) unless cell.west
                    img.line(x2, y1, x2, y2, wall) unless cell.linked?(cell.east)
                    img.line(x1, y2, x2, y2, wall) unless cell.linked?(cell.south)
                end
            end
        end

        img
    end

    def self.merge_vertical(*grids)
        rows = grids.first.rows
        merged = Array.new(rows, [])
        grids.each do |grid|
            i = 0
            length = merged[0].size

            grid.each_row do |row|
                unless merged[i].empty?
                    old_eastern_end = merged[i].last
                    new_eastern_end = row.first
                    old_eastern_end.east = new_eastern_end
                    new_eastern_end.west = old_eastern_end
                end

                merged[i] += row
                i += 1
            end

            link_row = merged[rand(rows)]
            link_row[length-1].link(link_row[length])
        end

        Grid.new(merged)
    end

    def self.merge_horizontal(*grids)
        merged = []
        puts merged
        grids.each do |grid|
            grid.each_row do |row|
                new_row = row.clone
                last_row = merged.last

                if last_row
                    last_row.zip(new_row).each do |pair|
                        pair[0].south = pair[1]
                        pair[1].north = pair[0]
                    end

                    index = rand(last_row.size)
                    last_row[index].link(new_row[index])
                end

                merged << new_row
            end
        end

        Grid.new(merged)
    end
end

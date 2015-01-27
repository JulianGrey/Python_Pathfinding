def find_adjacent_cells(current_cell, grid):
    cell_x = current_cell[0]
    cell_y = current_cell[1]

    cells = []
    adj_cells = []

    cells.append([cell_x - 1, cell_y, True, None])
    cells.append([cell_x + 1, cell_y, True, None])
    cells.append([cell_x, cell_y - 1, True, None])
    cells.append([cell_x, cell_y + 1, True, None])

    for cell in cells:
        if cell in grid:
            adj_cells.append(cell)
    return adj_cells

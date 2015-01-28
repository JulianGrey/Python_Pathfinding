def find_adjacent_cells(current_cell, grid, distance_moved):
    cell_x = current_cell[0]
    cell_y = current_cell[1]
    cells = []
    adj_cells = []

    cells.append([cell_x - 1, cell_y, True, distance_moved + 1, 0, None])
    cells.append([cell_x + 1, cell_y, True, distance_moved + 1, 0, None])
    cells.append([cell_x, cell_y - 1, True, distance_moved + 1, 0, None])
    cells.append([cell_x, cell_y + 1, True, distance_moved + 1, 0, None])

    for cell in cells:
        cell_base = [cell[0], cell[1], cell[2], 0, cell[4], cell[5]]
        if cell_base in grid:
            adj_cells.append(cell)
    return adj_cells

from base_maps import MapWithObstacles, MapNoObstacles


def find_adjacent_cells(current_cell, grid):
    cell_x = current_cell[0]
    cell_y = current_cell[1]

    cells = []
    adj_cells = []

    cells.append((cell_x - 1, cell_y, True))
    cells.append((cell_x + 1, cell_y, True))
    cells.append((cell_x, cell_y - 1, True))
    cells.append((cell_x, cell_y + 1, True))

    for cell in cells:
        if cell in grid:
            adj_cells.append(cell)

    return adj_cells


def pathfinding():
    my_map = MapNoObstacles(12, 10)
    list_cells = my_map.build_map()

    start_cell = (0, 0, True)
    destination = (11, 9, True)

    open_cells = []
    closed_cells = []
    adj_cells = []
    current_cell = None

    open_cells.append(start_cell)
    closed_cells.append(start_cell)

    if current_cell is None:
        current_cell = closed_cells[-1]
        open_cells.remove(current_cell)

    while current_cell is not destination:
        adj_cells = find_adjacent_cells(current_cell, list_cells)

        for cell in adj_cells:
            if cell not in open_cells:
                open_cells.append(cell)

        selection = []
        next_cell = None
        next_cell_distance = None

        for cell in adj_cells:
            if cell not in closed_cells:
                selection.append(cell)

        for cell in selection:
            distance = (abs(destination[0] - cell[0]) +
                        abs(destination[1] - cell[1]))
            if next_cell is None:
                next_cell = cell
                next_cell_distance = distance
            else:
                if distance < next_cell_distance:
                    next_cell = cell
                    next_cell_distance = distance

        current_cell = next_cell
        closed_cells.append(current_cell)
        open_cells.remove(current_cell)

        if current_cell == destination:
            break

    print 'Start position: ' + str(start_cell) + \
          ' | Destination: ' + str(destination)
    print closed_cells


pathfinding()

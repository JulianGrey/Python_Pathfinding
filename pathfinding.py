from base_maps import MapWithObstacles, MapNoObstacles


def find_adjacent_cells(current_cell):
    cell_x = current_cell[0]
    cell_y = current_cell[1]

    cell_left = (cell_x - 1, cell_y)
    cell_right = (cell_x + 1, cell_y)
    cell_up = (cell_x, cell_y - 1)
    cell_down = (cell_x, cell_y + 1)

    return [cell_left, cell_right, cell_up, cell_down]


def pathfinding():
    my_map = MapoObstacles(12, 10)
    my_map.draw_map()
    list_cells = my_map.list_grid_cells

    start_cell = (15, 3)
    destination = (5, 7)

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
        adj_cells = find_adjacent_cells(current_cell)
        open_cells.extend(adj_cells)
        selection = []
        next_cell = None
        next_cell_distance = None

        for cell in adj_cells:
            if cell not in closed_cells:
                selection.append(cell)
        
        for cell in selection:
            distance = abs(destination[0] - cell[0]) + \
                       abs(destination[1] - cell[1])
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

    # print 'Start position: ' + str(start_cell) + \
    #       ' | Destination: ' + str(destination)
    # print closed_cells


pathfinding()

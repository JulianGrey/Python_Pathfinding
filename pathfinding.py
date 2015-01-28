from adjacency import find_adjacent_cells
from base_maps import MapNoObstacles


start = [0, 0, True]
target = [11, 9, True]
my_map = MapNoObstacles(12, 10)


def find_path(defined_map, start, target):
    list_cells = defined_map.build_map()
    open_cells = []
    closed_cells = []
    adj_cells = []
    current_cell = []
    distance_moved = 0
    open_cells.append(start)
    closed_cells.append(start)

    if not current_cell:
        current_cell = closed_cells[-1]
        open_cells.remove(current_cell)

    while current_cell is not target:
        selection = []
        adj_cells = find_adjacent_cells(current_cell, list_cells)

        for cell in adj_cells:
            if cell not in open_cells:
                open_cells.append(cell)
            if cell not in closed_cells:
                selection.append(cell)

        current_cell = pathfinder(selection)
        if current_cell:
            current_cell_base = [
                current_cell[0], current_cell[1], current_cell[2]
            ]
        current_cell[3] = closed_cells[-1]
        closed_cells.append(current_cell_base)
        open_cells.remove(current_cell)
        distance_moved += 1

        if current_cell_base == target:
            break

    print('\nStart position: ' + str(start) +
          ' | Destination: ' + str(target) + '\n')
    for cell in closed_cells:
        print cell
    print distance_moved


def pathfinder(selection):
    next_cell = []
    next_cell_distance = None

    for cell in selection:
        distance = (abs(target[0] - cell[0]) +
                    abs(target[1] - cell[1]))
        if not next_cell:
            next_cell = cell
            next_cell_distance = distance
        else:
            if distance < next_cell_distance:
                next_cell = cell
                next_cell_distance = distance

    return next_cell


find_path(my_map, start, target)

from adjacency import find_adjacent_cells
# from base_maps import MapNoObstacles
from base_maps import MapWithObstacles


# start = [0, 0, True]
# target = [11, 9, True]
# my_map = MapNoObstacles(12, 10)
start = [0, 5, True]
target = [11, 5, True]
my_map = MapWithObstacles(12, 10)


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
        adj_cells = find_adjacent_cells(
            current_cell, list_cells, distance_moved)
        for cell in adj_cells:
            cell_base = [cell[0], cell[1], cell[2]]
            if cell_base not in open_cells:
                open_cells.append(cell)
            if cell_base not in closed_cells:
                selection.append(cell)

        current_cell = pathfinder(selection)
        if current_cell:
            current_cell_base = [
                current_cell[0], current_cell[1], current_cell[2]
            ]
        current_cell[5] = closed_cells[-1]
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
    next_cell_move_cost = None
    for cell in selection:
        cell[4] = (abs(target[0] - cell[0]) +
                   abs(target[1] - cell[1]))
        if not next_cell:
            next_cell = cell
            next_cell_move_cost = cell[4]
        else:
            if cell[4] < next_cell_move_cost:
                next_cell = cell
                next_cell_move_cost = cell[4]
    return next_cell


find_path(my_map, start, target)

# from time import sleep
from adjacency import find_adjacent_cells
# from base_maps import MapNoObstacles
from base_maps import MapWithObstacles


# start = [0, 0, True]
# target = [11, 9, True]
# my_map = MapNoObstacles(12, 10)
start = [2, 5, True]
target = [9, 5, True]
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
            current_cell, list_cells, distance_moved, target)
        # print '\nCurrent cell: ' + str(current_cell)
        for cell in adj_cells:
            cell_base = [cell[0], cell[1], cell[2]]
            if open_cells:
                if cell_base not in open_cells:
                    open_cells.append(cell)
                if cell_base not in closed_cells:
                    selection.append(cell)
                # sleep(0)
            else:
                if cell_base not in open_cells:
                    open_cells.append(cell)
                if cell_base not in closed_cells:
                    selection.append(cell)
        next_cell = []
        next_cell_f_score = None
        # print 'Selection: ' + str(selection)
        for cell in selection:
            cell_base = [cell[0], cell[1], cell[2]]
            if not next_cell:
                next_cell = cell
                next_cell_f_score = cell[3] + cell[4]
            else:
                for open_cell in open_cells:
                    open_cell_base = [open_cell[0], open_cell[1], open_cell[2]]
                    # print set(cell).intersection(open_cell)
                    # print('Considered cell: ' + str(cell) + ' | Open cell: '
                    #       + str(open_cell))
                    # print [i for i, j in zip(cell, open_cell) if i == j]
                    # print cell, open_cell
                    # print '\n'
                    # sleep(1)
                    if cell_base == open_cell_base:
                        cell_f_score = cell[3] + cell[4]
                        open_cell_f_score = open_cell[3] + open_cell[4]
                        # print open_cell_f_score, cell_f_score
                        if open_cell_f_score < cell_f_score:
                            open_cell_move_cost = open_cell[3]
                            closed_cells = closed_cells[
                                :(open_cell_move_cost - 1)
                            ]
                            closed_cells.append(open_cell)
                            next_cell = open_cell
                    else:
                        if cell[3] + cell[4] < next_cell_f_score:
                            next_cell = cell
                            next_cell_f_score = cell[3] + cell[4]
            # print 'Next cell: ' + str(next_cell)
        current_cell = next_cell
        if current_cell:
            current_cell_base = [
                current_cell[0], current_cell[1], current_cell[2]
            ]
        current_cell[5] = closed_cells[-1]
        closed_cells.append(current_cell_base)
        open_cells.remove(current_cell)
        distance_moved += 1
        # print 'Chosen cell: ' + str(closed_cells[-1])
        # print '\n\n'
        # sleep(2)
        if current_cell_base == target:
            break

    # print('\nStart position: ' + str(start) +
    #       ' | Destination: ' + str(target) + '\n')
    # for cell in closed_cells:
    #     print cell
    # print distance_moved


find_path(my_map, start, target)

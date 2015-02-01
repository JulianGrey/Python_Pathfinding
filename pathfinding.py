# from time import sleep
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
    open_list = []
    open_list_base = []
    closed_list = []
    adj_cells = []
    current_cell = []
    distance_moved = 0
    open_list.append(start)
    closed_list.append(start)
    if not current_cell:
        current_cell = closed_list[-1]
        open_list.remove(current_cell)

    while current_cell is not target:
        selection = []
        adj_cells = find_adjacent_cells(
            current_cell, list_cells, distance_moved, target)
        # print '\nCurrent cell: ' + str(current_cell)
        for cell in adj_cells:
            cell_base = [cell[0], cell[1], cell[2]]
            if cell_base not in closed_list:
                if cell_base in open_list_base:
                    # if the adjacent cell is found in the open list
                    found_cell = [obj for obj in open_list
                                  if obj[0] == cell_base[0]
                                  and obj[1] == cell_base[1]][0]
                    # print found_cell
                    # print closed_list.index(found_cell)
                    if (found_cell[3] + found_cell[4] <
                            cell[3] + cell[4]):
                        # Found cell does not have a parent set to it
                        # print 'Better path found'
                        pass
                else:
                    # print 'Not found'
                    pass
                if cell_base not in open_list:
                    open_list.append(cell)
                    open_list_base.append(cell_base)
                if cell_base not in closed_list:
                    selection.append(cell)
            else:
                pass
        # sleep(1)

        next_cell = []
        next_cell_f_score = None
        # print 'Selection: ' + str(selection)
        for cell in selection:
            cell_base = [cell[0], cell[1], cell[2]]
            if not next_cell:
                next_cell = cell
                next_cell_f_score = cell[3] + cell[4]
            else:
                for open_cell in open_list:
                    open_cell_base = [open_cell[0], open_cell[1], open_cell[2]]
                    if cell_base == open_cell_base:
                        cell_f_score = cell[3] + cell[4]
                        open_cell_f_score = open_cell[3] + open_cell[4]
                        # print open_cell_f_score, cell_f_score
                        if open_cell_f_score < cell_f_score:
                            open_cell_move_cost = open_cell[3]
                            closed_list = closed_list[
                                :(open_cell_move_cost - 1)
                            ]
                            closed_list.append(open_cell)
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
        current_cell[5] = closed_list[-1]
        closed_list.append(current_cell_base)
        open_list.remove(current_cell)
        distance_moved += 1
        # print current_cell
        # print 'Chosen cell: ' + str(closed_list[-1])
        # print '\n\n'
        # sleep(2)
        if current_cell_base == target:
            break

    # print('\nStart position: ' + str(start) +
    #       ' | Destination: ' + str(target) + '\n')
    # for cell in closed_list:
    #     print cell
    # print distance_moved


find_path(my_map, start, target)

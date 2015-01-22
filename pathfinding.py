class Map():
    list_grid_cells = []
    for y in range(6):
        for x in range(8):
            list_grid_cells.append((x, y))


def pathfinding():
    my_map = Map()
    start_cell = (1, 4)
    destination = (6, 3)
    open_cells = []
    closed_cells = []

    for cell in my_map.list_grid_cells:
        if cell[0] == start_cell[0] and cell[1] == start_cell[1]:
            my_map.list_grid_cells.remove(cell)
    print my_map.list_grid_cells


pathfinding()

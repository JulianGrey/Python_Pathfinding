class Map():
    list_grid_cells = []
    num_cols = 8
    num_rows = 6

    for y in range(num_rows):
        for x in range(num_cols):
            list_grid_cells.append((x, y))

    def draw_map():
        pass


def find_adjacent_cell(cell):
    pass



def pathfinding():
    my_map = Map()
    list_cells = my_map.list_grid_cells
    start_cell = (1, 4)
    destination = (6, 3)
    open_cells = []
    closed_cells = []

    if start_cell in list_cells:
        list_cells.remove(start_cell)

    # for cell in my_map.list_grid_cells:
    #     if cell[0] == start_cell[0] and cell[1] == start_cell[1]:
    #         my_map.list_grid_cells.remove(cell)
    print my_map.list_grid_cells


pathfinding()

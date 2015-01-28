class MapNoObstacles(object):
    def __init__(self, columns=0, rows=0):
        self.num_cols = columns
        self.num_rows = rows
        self.list_grid_cells = []

    def build_map(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                self.list_grid_cells.append([x, y, True, 0, 0, None])
        return self.list_grid_cells

    def draw_map(self):
        list_grid_cells = self.build_map()
        for cell in list_grid_cells:
            if (cell[0] + 1) % self.num_cols == 0:
                if cell[2] is False:
                    print 'x'
                else:
                    print 'o'
            else:
                if cell[2] is False:
                    print 'x',
                else:
                    print 'o',


class MapWithObstacles(object):
    def __init__(self, columns=0, rows=0):
        self.num_cols = columns
        self.num_rows = rows
        self.list_grid_cells = []

    def build_map(self):
        for y in range(self.num_rows):
            for x in range(self.num_cols):
                if x == 5:
                    if y > 0 and y < 9:
                        self.list_grid_cells.append(
                            [x, y, False, 0, 0, None]
                        )
                    else:
                        self.list_grid_cells.append(
                            [x, y, True, 0, 0, None]
                        )
                else:
                    self.list_grid_cells.append([x, y, True, 0, 0, None])
        return self.list_grid_cells

    def draw_map(self):
        list_grid_cells = self.build_map()
        for cell in list_grid_cells:
            if (cell[0] + 1) % self.num_cols == 0:
                if cell[2] is False:
                    print 'x'
                else:
                    print 'o'
            else:
                if cell[2] is False:
                    print 'x',
                else:
                    print 'o',

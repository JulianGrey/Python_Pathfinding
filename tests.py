import unittest

from base_maps import MapNoObstacles
from pathfinding import find_adjacent_cells


class TestMap(unittest.TestCase):

    def setUp(self):
        self.test_map = MapNoObstacles(10, 10)

    def test_map_exists(self):
        self.assertTrue(self.test_map)

    def test_map_size(self):
        self.assertEqual(self.test_map.num_cols, 10)
        self.assertEqual(self.test_map.num_rows, 10)

    def test_map_cells(self):
        self.assertEqual(self.test_map.num_cols * self.test_map.num_rows,
                         len(self.test_map.build_map()))

    def test_cell_exists(self):
        cell = [5, 5, True, 0, 0, None]
        self.assertIn(cell, self.test_map.build_map())

    def test_cell_does_not_exist(self):
        cell = [11, 3, True, 0, 0, None]
        self.assertNotIn(cell, self.test_map.build_map())


class TestPathfinding(unittest.TestCase):

    def setUp(self):
        self.test_map = MapNoObstacles(10, 10)

    def test_adjacent_cells(self):
        cell = [5, 5, True, 0, 0, None]
        north_cell = [5, 4, True, 1, 0, None]
        east_cell = [6, 5, True, 1, 0, None]
        south_cell = [5, 6, True, 1, 0, None]
        west_cell = [4, 5, True, 1, 0, None]
        self.assertIn(north_cell,
                      find_adjacent_cells(cell,
                                          self.test_map.build_map(),
                                          0))
        self.assertIn(east_cell,
                      find_adjacent_cells(cell,
                                          self.test_map.build_map(),
                                          0))
        self.assertIn(south_cell,
                      find_adjacent_cells(cell,
                                          self.test_map.build_map(),
                                          0))
        self.assertIn(west_cell,
                      find_adjacent_cells(cell,
                                          self.test_map.build_map(),
                                          0))


if __name__ == '__main__':
    unittest.main()

import unittest

from base_maps import MapWithObstacles, MapNoObstacles
# from pathfinder import pathfinding


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
        cell = (5, 5, True)
        self.assertIn(cell, self.test_map.build_map())

    def test_cell_does_not_exist(self):
        cell = (11, 3, True)
        self.assertNotIn(cell, self.test_map.build_map())


class TestPathfinding(unittest.TestCase):
    
    def setUp(self):
        self.test_map = MapNoObstacles(10, 10)


if __name__ == '__main__':
    unittest.main()

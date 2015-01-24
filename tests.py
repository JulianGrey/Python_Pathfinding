import unittest

from base_maps import MapWithObstacles, MapNoObstacles


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


class TestPathfinding(unittest.TestCase):
    pass


if __name__ == '__main__':
    unittest.main()

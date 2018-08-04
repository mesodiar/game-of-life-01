import unittest

from gof import get_neighbors_of


class GameOfLifeTest(unittest.TestCase):
    def test_get_neighbors_of_cell_one_one_should_return_neighbors(self):
        cell = (1, 1)
        result = get_neighbors_of(cell)
        self.assertEqual(result,
        {(0, 0), (0, 1), (0, 2),
        (1, 0),         (1, 2),
        (2, 0), (2, 1), (2, 2)
        })


if __name__ == '__main__':
    unittest.main()

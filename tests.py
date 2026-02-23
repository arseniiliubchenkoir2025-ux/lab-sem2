import unittest
from sem2.lab1.main import zigzag


class TestZigZag(unittest.TestCase):

    def test_5x5(self):
        matrix = [[(i * 5 + j + 1) for j in range(5)] for i in range(5)]
        expected = [1, 2, 6, 11, 7, 3, 4, 8, 12, 16,
                    21, 17, 13, 9, 5, 10, 14, 18,
                    22, 23, 19, 15, 20, 24, 25]
        self.assertEqual(zigzag(matrix), expected)

    def test_2x4(self):
        matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
        expected = [1, 2, 5, 6, 3, 4, 7, 8]
        self.assertEqual(zigzag(matrix), expected)

    def test_n_1(self):
        matrix = [[1], [2], [3], [4]]
        self.assertEqual(zigzag(matrix), [1, 2, 3, 4])

    def test_m_1(self):
        matrix = [[1, 2, 3, 4, 5, 6]]
        self.assertEqual(zigzag(matrix), [1, 2, 3, 4, 5, 6])

    def test_1x1(self):
        self.assertEqual(zigzag([[42]]), [42])

    def test_3x3(self):
        matrix = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        expected = [1, 2, 4, 7, 5, 3, 6, 8, 9]
        self.assertEqual(zigzag(matrix), expected)


if __name__ == "__main__":
    unittest.main()
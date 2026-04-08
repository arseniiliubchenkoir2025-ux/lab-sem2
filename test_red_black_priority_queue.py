import unittest
from .red_black_priority_queue import RedBlackPriorityQueue


class TestRedBlackPriorityQueue(unittest.TestCase):
    def setUp(self):
        self.q = RedBlackPriorityQueue()

    def test_peek_empty(self):
        self.assertIsNone(self.q.peek())

    def test_pop_empty(self):
        self.assertIsNone(self.q.pop_max())

    def test_insert_and_peek(self):
        self.q.insert("A", 5)
        self.q.insert("B", 2)
        self.q.insert("C", 8)
        self.assertEqual(self.q.peek(), ("C", 8))

    def test_pop_max(self):
        self.q.insert("A", 5)
        self.q.insert("B", 2)
        self.q.insert("C", 8)
        self.q.insert("D", 6)

        self.assertEqual(self.q.pop_max(), ("C", 8))
        self.assertEqual(self.q.peek(), ("D", 6))

    def test_multiple_pop(self):
        self.q.insert("A", 5)
        self.q.insert("B", 2)
        self.q.insert("C", 8)
        self.q.insert("D", 6)

        self.assertEqual(self.q.pop_max(), ("C", 8))
        self.assertEqual(self.q.pop_max(), ("D", 6))
        self.assertEqual(self.q.pop_max(), ("A", 5))
        self.assertEqual(self.q.pop_max(), ("B", 2))
        self.assertIsNone(self.q.pop_max())

    def test_same_priority(self):
        self.q.insert("A", 5)
        self.q.insert("B", 5)
        self.q.insert("C", 5)

        first = self.q.pop_max()
        second = self.q.pop_max()
        third = self.q.pop_max()

        self.assertEqual(first[1], 5)
        self.assertEqual(second[1], 5)
        self.assertEqual(third[1], 5)
        self.assertIsNone(self.q.pop_max())


if __name__ == "__main__":
    unittest.main()
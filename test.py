import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

from main import BinaryTree


class TestTreeVisual(unittest.TestCase):

    def setUp(self):
        self.test_file = os.path.join(current_dir, "input.txt")
        self.tree_instance = BinaryTree()

        if os.path.exists(self.test_file):
            self.tree_instance.load_from_file(self.test_file)

    def test_rendering(self):
        if self.tree_instance:
            self.tree_instance.show_preorder()
            self.tree_instance.display_tree()
            self.tree_instance.check_balance()


if __name__ == "__main__":
    unittest.main()
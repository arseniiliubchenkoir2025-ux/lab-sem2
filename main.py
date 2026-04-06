import os


class BinaryTree:
    def __init__(self, val=0):
        self.value = val
        self.left = None
        self.right = None

    def _parse_input(self, data_list):
        if not data_list:
            return None

        token = data_list.pop(0)
        if token == "Null":
            return None

        node = BinaryTree(int(token))
        node.left = self._parse_input(data_list)
        node.right = self._parse_input(data_list)
        return node

    def _calculate_height(self, node):
        if not node:
            return 0
        return max(self._calculate_height(node.left), self._calculate_height(node.right)) + 1

    def _write_to_grid(self, grid, r, c, val):
        txt = str(val)
        shift = len(txt) // 2
        for i, char in enumerate(txt):
            pos_c = c + i - shift
            if 0 <= r < len(grid) and 0 <= pos_c < len(grid[0]):
                grid[r][pos_c] = char

    def _render_node(self, node, grid, r, c, mode, step_y, step_x):
        if not node:
            return

        self._write_to_grid(grid, r, c, node.value)

        val_width = len(str(node.value))
        l_edge = c - (val_width // 2) - 1
        r_edge = c + (val_width - val_width // 2)
        next_step_y = max(2, step_y - 2)

        if mode == "root":
            if node.left:
                grid[r][l_edge] = "-"
                self._render_node(node.left, grid, r, c - step_x, "left", step_y, step_x)
            if node.right:
                grid[r][r_edge] = "-"
                self._render_node(node.right, grid, r, c + step_x, "right", step_y, step_x)

        elif mode == "left":
            if node.left:
                grid[r - 1][l_edge] = "\\"
                self._render_node(node.left, grid, r - step_y, c - step_x, "left", next_step_y, step_x)
            if node.right:
                grid[r + 1][l_edge] = "/"
                self._render_node(node.right, grid, r + step_y, c - step_x, "left", next_step_y, step_x)

        elif mode == "right":
            if node.left:
                grid[r - 1][r_edge] = "/"
                self._render_node(node.left, grid, r - step_y, c + step_x, "right", next_step_y, step_x)
            if node.right:
                grid[r + 1][r_edge] = "\\"
                self._render_node(node.right, grid, r + step_y, c + step_x, "right", next_step_y, step_x)

    def load_from_file(self, path):
        if not os.path.exists(path):
            return
        try:
            with open(path, "r") as f:
                tokens = f.read().split()
            if tokens:
                first = tokens.pop(0)
                if first != "Null":
                    self.value = int(first)
                    self.left = self._parse_input(tokens)
                    self.right = self._parse_input(tokens)
        except Exception:
            pass

    def display_tree(self):
        h = self._calculate_height(self)
        h_size, w_size = 45, 80
        canvas = [[" " for _ in range(w_size)] for _ in range(h_size)]

        self._render_node(self, canvas, h_size // 2, w_size // 2, "root", 6, 6)

        print("\n--- Візуалізація дерева ---")
        for row in canvas:
            line = "".join(row).rstrip()
            if line:
                print(line)

    def show_preorder(self):
        def traverse(n):
            if not n:
                print("Null", end=" ")
                return
            print(n.value, end=" ")
            traverse(n.left)
            traverse(n.right)

        print("Преордер обхід:", end=" ")
        traverse(self)
        print()

    def check_balance(self):
        def get_stat(n):
            if not n:
                return 0
            l_h = get_stat(n.left)
            r_h = get_stat(n.right)

            if l_h == -1 or r_h == -1 or abs(l_h - r_h) > 1:
                return -1
            return max(l_h, r_h) + 1

        is_ok = get_stat(self) != -1
        print(f"Дерево збалансоване: {is_ok}")
        return is_ok


# Запуск
if __name__ == "__main__":
    my_tree = BinaryTree()

    my_tree.load_from_file("input")
    my_tree.show_preorder()
    my_tree.display_tree()
    print("")
    my_tree.check_balance()
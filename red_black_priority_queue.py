class Node:
    def __init__(self, value, priority, color="R"):
        self.value = value
        self.priority = priority
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackPriorityQueue:
    def __init__(self):
        self.root = None

    def insert(self, value, priority):
        node = Node(value, priority)

        parent = None
        current = self.root

        while current is not None:
            parent = current
            if priority >= current.priority:
                current = current.left
            else:
                current = current.right

        node.parent = parent

        if parent is None:
            self.root = node
        elif priority >= parent.priority:
            parent.left = node
        else:
            parent.right = node

        self._fix_insert(node)

    def peek(self):
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        return current.value, current.priority

    def pop_max(self):
        if self.root is None:
            return None

        current = self.root
        while current.left is not None:
            current = current.left

        result = (current.value, current.priority)
        self._delete_node(current)
        return result

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left is not None:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y

    def _right_rotate(self, y):
        x = y.left
        y.left = x.right

        if x.right is not None:
            x.right.parent = y

        x.parent = y.parent

        if y.parent is None:
            self.root = x
        elif y == y.parent.right:
            y.parent.right = x
        else:
            y.parent.left = x

        x.right = y
        y.parent = x

    def _fix_insert(self, z):
        while z.parent is not None and z.parent.color == "R":
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right

                if y is not None and y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self._left_rotate(z)

                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self._right_rotate(z.parent.parent)
            else:
                y = z.parent.parent.left

                if y is not None and y.color == "R":
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self._right_rotate(z)

                    z.parent.color = "B"
                    z.parent.parent.color = "R"
                    self._left_rotate(z.parent.parent)

        self.root.color = "B"

    def _transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v

        if v is not None:
            v.parent = u.parent

    def _minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def _delete_node(self, z):
        if z.left is None:
            self._transplant(z, z.right)
        elif z.right is None:
            self._transplant(z, z.left)
        else:
            y = self._minimum(z.right)

            if y.parent != z:
                self._transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self._transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
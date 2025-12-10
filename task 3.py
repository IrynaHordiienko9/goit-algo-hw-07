class RBNode:
    def __init__(self, value, color='red'):
        self.value = value
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = RBNode(None, color='black')
        self.root = self.NIL

    def insert(self, value):
        new_node = RBNode(value)
        new_node.left = self.NIL
        new_node.right = self.NIL
        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if new_node.value < current.value:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node
        elif new_node.value < parent.value:
            parent.left = new_node
        else:
            parent.right = new_node

        new_node.color = 'red'
        self._fix_insert(new_node)

    def _recolor(self, node, uncle):
        node.parent.color = 'black'
        uncle.color = 'black'
        node.parent.parent.color = 'red'
        return node.parent.parent

    def _rotate_and_recolor(self, node, rotate_func):
        rotate_func(node.parent)
        node.parent.color = 'black'
        node.parent.parent.color = 'red'

    def _fix_insert(self, node):
        while node != self.root and node.parent.color == 'red':
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 'red':
                    node = self._recolor(node, uncle)
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self._left_rotate(node)
                    self._rotate_and_recolor(node, self._right_rotate)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 'red':
                    node = self._recolor(node, uncle)
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self._right_rotate(node)
                    self._rotate_and_recolor(node, self._left_rotate)
        self.root.color = 'black'

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
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
        if x.right != self.NIL:
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

    def tree_sum(self, node=None):
        if node is None:
            node = self.root
        if node == self.NIL or node.value is None:
            return 0
        return node.value + self.tree_sum(node.left) + self.tree_sum(node.right)


if __name__ == "__main__":
    tree = RedBlackTree()
    tree.insert(10)
    tree.insert(5)
    tree.insert(15)
    tree.insert(7)
    tree.insert(20)
    print(tree.tree_sum())
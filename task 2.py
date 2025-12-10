class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root


def find_min_with_path(node):
    path = []
    current = node
    while current.left is not None:
        path.append(current.key)
        current = current.left
    path.append(current.key)
    return current.key, path


def print_tree(node, min_value, prefix="", is_left=True):
    if node is not None:
        print_tree(node.right, min_value, prefix + ("│   " if is_left else "    "), False)
        marker = " *" if node.key == min_value else ""
        print(prefix + ("└── " if is_left else "┌── ") + str(node.key) + marker)
        print_tree(node.left, min_value, prefix + ("    " if is_left else "│   "), True)


root = None
for value in [20, 8, 22, 4, 12, 10, 14]:
    root = insert(root, value)

min_value, path = find_min_with_path(root)
print(f"Min value: {min_value}")
print(f"Path to the minimum element: {path}\n")
print("Tree visualization (minimum marked *):")
print_tree(root, min_value)

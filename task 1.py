class AVLNode:
    def __init__(self, key, data=None):
        self.key = key
        self.data = data
        self.left = None
        self.right = None
        self.height = 1


def get_height(node):
    return node.height if node else 0


def update_height(node):
    node.height = 1 + max(get_height(node.left), get_height(node.right))


def rotate_right(y):
    x = y.left
    T2 = x.right
    x.right = y
    y.left = T2
    update_height(y)
    update_height(x)
    return x


def rotate_left(x):
    y = x.right
    T2 = y.left
    y.left = x
    x.right = T2
    update_height(x)
    update_height(y)
    return y


def get_balance(node):
    return get_height(node.left) - get_height(node.right) if node else 0


def insert(node, key, data=None):
    if not node:
        return AVLNode(key, data)
    if key < node.key:
        node.left = insert(node.left, key, data)
    elif key > node.key:
        node.right = insert(node.right, key, data)
    else:
        return node  

    update_height(node)
    balance = get_balance(node)

    if balance > 1 and key < node.left.key:
        return rotate_right(node)
    if balance < -1 and key > node.right.key:
        return rotate_left(node)
    if balance > 1 and key > node.left.key:
        node.left = rotate_left(node.left)
        return rotate_right(node)
    if balance < -1 and key < node.right.key:
        node.right = rotate_right(node.right)
        return rotate_left(node)
    return node


def find_max_recursive(node, path=None):
    if path is None:
        path = []
    if node is None:
        return None, path
    path.append(node.key)
    if node.right is None:
        return node, path
    return find_max_recursive(node.right, path)


root = None
for key, data in [(10, "root"), (5, "left"), (20, "right"), (15, "right-left"), (25, "right-right"), (30, "max")]:
    root = insert(root, key, data)

max_node, path = find_max_recursive(root)
if max_node:
    print(f"The largest key: {max_node.key}, data: {max_node.data}")
    print(f"Path to the largest node: {path}")
else:
    print("The tree is empty")

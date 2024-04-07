class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None


def in_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        print(root.key)
        in_order_traversal(root.right)


def pre_order_traversal(root):
    if root is not None:
        print(root.key)
        in_order_traversal(root.left)
        in_order_traversal(root.right)


def post_order_traversal(root):
    if root is not None:
        in_order_traversal(root.left)
        in_order_traversal(root.right)
        print(root.key)


def breadth_first_search(root):
    result = []
    sum = 0
    if root is None:
        return result
    queue = [root]
    # sum = 0
    while queue:
       
        node = queue.pop(0)
        result.append(node.key)
        sum += node.key
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    print(sum)


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.right = Node(5)
    # in_order_traversal(root)
    # pre_order_traversal(root)
    # post_order_traversal(root)
    breadth_first_search(root)

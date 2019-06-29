"""
This solution traverse the tree two times, so the complexity of this solution is O(2n)
We ignore the constants, so the final complexity of this solution is O(n)
"""


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


def node_path(root, path, key):
    if root is None:
        return False

    path.append(root.key)

    if root.key == key:
        return True

    if (
        (root.left and node_path(root.left, path, key)) or
        (root.right and node_path(root.right, path, key))
    ):
        return True

    path.pop()
    return False


def find_lca(root, first_key, second_key):
    first_key_path = []
    second_key_path = []

    # populate node path
    node_path(root, first_key_path, first_key)
    node_path(root, second_key_path, second_key)

    if not(first_key_path and second_key_path):
        return None

    first_key_path_length = len(first_key_path)
    second_key_path_length = len(second_key_path)

    index = 0
    while index < first_key_path_length and index < second_key_path_length:
        if first_key_path[index] != second_key_path[index]:
            break
        index += 1
    return first_key_path[index - 1]


if __name__ == '__main__':
    # The tree from the question 3
    root = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)

    root.left = node2
    root.right = node3
    node2.left = node4
    node2.right = node5
    node3.left = node6
    node3.right = node7
    node4.left = node8
    node4.right = node9

    print(f'lca of 6 and 7 is {find_lca(root, 6, 7)}')
    print(f'lca of 3 and 7 is {find_lca(root, 3, 7)}')

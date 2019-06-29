import pytest
from problems.problem3 import node_path, find_lca, Node


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


class TestNodePath(object):
    @pytest.mark.parametrize(
        "key,expected", [
            (1, [1]),
            (9, [1, 2, 4, 9]),
            (6, [1, 3, 6]),
            (11, [])  # for non existent node array should be remain empty
        ]
    )
    def test_node_path(self, key, expected):
        path = []
        node_path(root, path, key)
        assert path == expected


class TestFindLCA(object):
    @pytest.mark.parametrize(
        "first_key,second_key,expected", [
            (11, 0, None),  # if no lca found function should return None
            (6, 7, 3),
            (3, 7, 3),
            (8, 7, 1),
            (1, 1, 1),
        ]
    )
    def test_node_path(self, first_key, second_key, expected):
        lca = find_lca(root, first_key, second_key)
        assert lca == expected

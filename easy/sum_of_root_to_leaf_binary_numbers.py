# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        paths = []

        def get_paths(node, current):

            if node is None:
                return

            if not node.left and not node.right:
                paths.append(current + [node.val])
            else:
                get_paths(node.left, current + [node.val])
                get_paths(node.right, current + [node.val])

        get_paths(root, [])

        paths_sum = 0

        def bin_to_deci(num):
            n = len(num) - 1
            deci = 0
            for index, digit in enumerate(num):
                deci += digit * (2 ** (n - index))
            return deci

        for path in paths:
            paths_sum += bin_to_deci(path)

        return paths_sum
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        # first traverse the both the trees
        full_list = self.get_tree_vals(root1) + self.get_tree_vals(root2)
        return sorted(full_list)

    @classmethod
    def get_tree_vals(cls, root: TreeNode):
        if root == None:
            return []

        left_list = cls.get_tree_vals(root.left)
        right_list = cls.get_tree_vals(root.right)
        return left_list + [root.val] + right_list
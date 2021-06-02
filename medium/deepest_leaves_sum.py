# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        nodequeue = [root]
        dlsum = f = 0
        obj = {}
        while f < len(nodequeue):
            node = nodequeue[f]
            f += 1
            if node.right is not None or node.left is not None:
                obj = {level: [node.left, node.right]}

            if node.right is None and node.left is None:
                dlsum += node.val
            else:
                if node.left is not None:
                    nodequeue.append(node.left)

                if node.right is not None:
                    nodequeue.append(node.right)

        return dlsum


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

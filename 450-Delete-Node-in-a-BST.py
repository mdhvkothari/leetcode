from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def cal_most_right_node(self, node: TreeNode) -> TreeNode:
        if node.right == None:
            return node
        return self.cal_most_right_node(node.right)

    def helper(self, node: TreeNode) -> TreeNode:
        if node.left == None:
            return node.right
        elif node.right == None:
            return node.left
        right_child = node.right
        most_left_right_child = self.cal_most_right_node(node.left)
        most_left_right_child.right = right_child
        return node.left

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return 
        if root.val == key:
            return self.helper(root)
        result = root
        while root:
            if root.val > key:
                if root.left and root.left.val == key:
                    root.left = self.helper(root.left)
                    break
                else:
                    root = root.left
            else:
                if root.right and root.right.val == key:
                    root.right = self.helper(root.right)
                    break
                else:
                    root = root.right
        return result

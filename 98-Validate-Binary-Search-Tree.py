from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def inOrder(self, arr: List[int], root: TreeNode):
        if not root:
            return
        self.inOrder(arr, root.left)
        arr.append(root.val)
        self.inOrder(arr, root.right)

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        self.inOrder(arr, root)
        for i in range(0, len(arr)-1):
            if arr[i] >= arr[i+1]:
                return False
        return True

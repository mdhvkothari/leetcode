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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        self.inOrder(arr, root)
        return arr[k-1]

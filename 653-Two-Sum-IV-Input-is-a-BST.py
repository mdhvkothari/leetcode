from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order(self, root: TreeNode, arr: List[int]) -> None:
        if not root:
            return 
        self.in_order(root.left, arr)
        arr.append(root.val)
        self.in_order(root.right, arr)

    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        arr = []
        self.in_order(root, arr)
        i, j = 0, len(arr) - 1
        while i < j:
            curr_sum = arr[i] + arr[j]
            if curr_sum == k:
                return True
            elif curr_sum < k:
                i += 1
            elif curr_sum > k:
                j -= 1
        return False

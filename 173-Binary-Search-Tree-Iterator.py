from typing import Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.arr = []
        self.in_order(root)
        self.counter = 0

    def in_order(self, root: TreeNode) -> None:
        if not root:
            return 
        self.in_order(root.left)
        self.arr.append(root.val)
        self.in_order(root.right)

    def next(self) -> int:
        val = self.arr[self.counter]
        self.counter += 1
        return val

    def hasNext(self) -> bool:
        return self.counter <= len(self.arr) - 1

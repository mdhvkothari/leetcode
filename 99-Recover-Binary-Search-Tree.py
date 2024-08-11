from typing import Optional, List, Tuple

"""
    There are only two cases
        case 1:
            The violated pairs are adjacent to each other
            1 2 3 4 5 6 7
            1 3 2 4 5 6 7 (3 and 2)
            [(3,2)]
        
        case 2:
            The violated pairs are not adjacent to each other
            1 2 3 4 5 6 7
            1 6 3 4 5 2 7 (6 and 2)
            [(6,3), (5,2)]
"""


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    
    def in_order(self, root: Optional[TreeNode], violated_pairs: List[Tuple[TreeNode, TreeNode]], prev: List[Optional[TreeNode]]) -> None:
        if not root:
            return
        self.in_order(root.left, violated_pairs, prev)
        if prev[0] and root.val < prev[0].val:
            violated_pairs.append((prev[0], root))
        prev[0] = root
        self.in_order(root.right, violated_pairs, prev)
    
    def get_violated_pairs(self, violated_pairs: List[Tuple[TreeNode, TreeNode]]) -> Tuple[Optional[TreeNode], Optional[TreeNode]]:
        if len(violated_pairs) == 1:
            return violated_pairs[0]
        return violated_pairs[0][0], violated_pairs[1][1]
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        violated_pairs = []
        prev = [None]
        self.in_order(root, violated_pairs, prev)
        a, b = self.get_violated_pairs(violated_pairs)
        a.val, b.val = b.val, a.val

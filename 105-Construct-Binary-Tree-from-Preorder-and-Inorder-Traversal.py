from typing import List, Optional


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build(self, pre_order, pre_start, pre_end, in_order, in_start, in_end, in_order_map):
        if pre_start > pre_end or in_start > in_end:
            return None
        root = TreeNode(pre_order[pre_start]) 
        in_root = in_order_map[root.val]
        num_left = in_root - in_start
        root.left = self.build(pre_order, pre_start+1, pre_start+num_left, in_order, in_start, in_root-1, in_order_map)
        root.right = self.build(pre_order, pre_start+num_left+1, pre_end, in_order, in_root+1, in_end, in_order_map)
        return root

    def buildTree(self, pre_order: List[int], in_order: List[int]) -> Optional[TreeNode]:
        if not pre_order or not in_order:
            return None
        in_order_map = {val: index for index, val in enumerate(in_order)}
        return self.build(pre_order, 0, len(pre_order)-1, in_order, 0, len(in_order)-1, in_order_map)
        
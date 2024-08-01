from typing import Optional, List


class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def build(self, in_order, in_order_start, in_order_end, post_order, post_order_start, post_order_end, in_order_map):
        if in_order_start > in_order_end or post_order_start > post_order_end:
            return None
        root = TreeNode(post_order[post_order_end])
        index = in_order_map[post_order[post_order_end]]
        num_left = index - in_order_start
        root.left = self.build(in_order, in_order_start, index-1, post_order, post_order_start, post_order_start+num_left-1, in_order_map)
        root.right = self.build(in_order, index+1, in_order_end, post_order, post_order_start+num_left, post_order_end-1, in_order_map)
        return root

    def buildTree(self, in_order: List[int], post_order: List[int]) -> Optional[TreeNode]:
        if len(in_order) != len(post_order):
            return None
        in_order_map = {val: index for index, val in enumerate(in_order)}
        return self.build(in_order, 0, len(in_order)-1, post_order, 0, len(post_order)-1, in_order_map)

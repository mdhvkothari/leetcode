from typing import Optional



'''
    If some how we will find the index of left most and the right most 
    then we can simply find the width of the tree with the help of (rightIndex - leftIndex + 1)
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



class Solution:

    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result, q = 0, [(root, 0)]
        while q:
            length = len(q)
            _, level = q[0]
            for i in range(length):
                node, index = q.pop(0)
                if node.left:
                    q.append((node.left, 2*index))
                if node.right:
                    q.append((node.right, 2*index+1))
            result = max(result, index-level + 1)
        return result



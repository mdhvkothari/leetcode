from typing import List


class Solution:

    def fun(self, root, level: int, ds: List[int]) -> None:
        if not root:
            return
        if len(ds) == level:
            ds.append(root.val)
        self.fun(root.right, level+1, ds)
        self.fun(root.left, level+1, ds)
    
    def rightSideView(self, root) -> List[int]:
        result = []
        if not root:
            return result
        self.fun(root, 0, result)
        return result


############## 
'''
    For left view just put root.left above root.right
'''
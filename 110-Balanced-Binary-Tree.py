
class Solution:

    def dfs(self, root) -> int:
        if not root: return 0
        left = self.dfs(root.left)
        if left == -1: return -1
        right = self.dfs(root.right)
        if right == -1: return -1
        if abs(left-right) > 1:
            return -1
        return max(left, right) + 1

    def isBalanced(self, root) -> bool:
        return self.dfs(root) != -1

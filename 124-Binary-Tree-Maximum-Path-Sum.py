

class Solution:

    def calSum(self, root, result):
        if not root:
            return 0
        leftSum = max(0, self.calSum(root.left, result))
        rightSum = max(0, self.calSum(root.right, result))
        result[0] = max(result[0], leftSum+rightSum+root.val)
        return root.val + max(leftSum, rightSum)

    def maxPathSum(self, root) -> int:
        result = [float('-inf')]
        self.calSum(root, result)
        return result[0]
        
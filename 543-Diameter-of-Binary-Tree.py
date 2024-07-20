class Solution:
    def calHeight(self, root, height):
        if not root:
            return 0
        leftHeight = self.calHeight(root.left, height)
        rightHeight = self.calHeight(root.right, height)
        height[0] = max(height[0], leftHeight+rightHeight )
        return 1 + max(leftHeight, rightHeight)

    def diameterOfBinaryTree(self, root) -> int:
        height = [0]
        self.calHeight(root, height)
        return height[0]
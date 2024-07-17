from typing import List



##### Two ways to traverse a tree 1. Recursive 2. Iterative ######


def preOrderTraversal(root) -> List[int]:
    result = []
    def dfs(root, result):
        if root:
            result.append(root.val)
            dfs(root.left, result)
            dfs(root.right, result)
    dfs(root, result)
    return result

######################################################################################

def preOrderTraversal(root) -> List[int]:
    res = []
    stack = [root]
    while stack:
        currentNode = stack.pop()
        if currentNode:
            res.append(currentNode.val)
            stack.append(currentNode.right)
            stack.append(currentNode.left)
    return res



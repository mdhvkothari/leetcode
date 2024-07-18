from typing import List


def levelOrder(root) -> List[List[int]]:
    if not root:
        return[]
    queue = [root]
    result = []
    while queue:
        size = len(queue)
        temp = []
        for i in range(size):
            node = queue.pop(0)
            temp.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(temp)
    return result

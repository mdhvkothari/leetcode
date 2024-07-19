###### There are two ways to get the max height of the binary tree ###############


#### 1. Using Level order traversal

def maxDepth(root) -> int:
    if not root:
        return 0
    queue = [root]
    count = 0
    while queue:
        length = len(queue)
        count += 1
        for i in range(length):
            node = queue.pop(0)
            if node and node.left:
                queue.append(node.left)
            if node and node.right:
                queue.append(node.right)
    return count



#### 2. Using recursion
def maxDepth(root) -> int:
    if not root: return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return 1 + max(left, right)



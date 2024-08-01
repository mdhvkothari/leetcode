

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return ""
        q, res = [root], []
        while q:
            node = q.pop(0)
            if node:
                res.append(str(node.val))
                q.append(node.left)
                q.append(node.right)
            else:
                res.append("None")
        return ",".join(res)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        arr = data.split(",")
        root = TreeNode(int(arr[0]))
        q, index = [root], 1
        while q:
            node = q.pop(0)
            if arr[index] != "None":
                node.left = TreeNode(int(arr[index]))
                q.append(node.left)
            index += 1
            if arr[index] != "None":
                node.right = TreeNode(int(arr[index]))
                q.append(node.right)
            index += 1
        return root 

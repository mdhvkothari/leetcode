from typing import List


## logic ##
'''
    we are maintain one flag variable when it is 1 then we have add temp array as a reverse 
    else as it as and this is a Level Order Traversal
'''
###########


class Solution:
    def zigzagLevelOrder(self, root) -> List[List[int]]:
        if not root:
            return []
        flag, result, q = 0, [], [root]
        while q:
            length = len(q)
            temp = []
            for i in range(length):
                node = q.pop(0)
                temp.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            if flag == 1:
                temp = temp[::-1]
                flag = 0
            else:
                flag = 1
            result.append(temp)
        return result


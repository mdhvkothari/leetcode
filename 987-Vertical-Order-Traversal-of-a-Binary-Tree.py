from typing import List
from collections import defaultdict, deque


class Solution:

    def verticalTraversal(root) -> List[List[int]]:
        q=deque()
        d=defaultdict(list)
        q.append([root,0,0])
        while q:
            node,c,r=q.popleft()
            d[c].append([r,node.val])
            if node.left:
                q.append([node.left,c-1,r+1])
            if node.right:
                q.append([node.right,c+1,r+1])
        ans=[]
        for i in sorted(d):
            temp=d[i]
            temp.sort()
            t=[]
            for j in temp:
                t.append(j[1])
            ans.append(t)
        return ans
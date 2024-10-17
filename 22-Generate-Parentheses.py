from typing import List

'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

                                    (0, 0, '')
								 	    |	
									(1, 0, '(')  
								   /           \
							(2, 0, '((')      (1, 1, '()')
							   /                 \
						(2, 1, '(()')           (2, 1, '()(')
						   /                       \
					(2, 2, '(())')                (2, 2, '()()')
						      |	                             |
					res.append('(())')             res.append('()()')
   
'''


class Solution:

    def dfs(self, left, right, s, res: List[int], n: int):
        if len(s) == n*2:
            res.append(s)
            return
        if left < n:
            self.dfs(left+1, right, s+"(", res, n)
        if right < left:
            self.dfs(left, right+1, s+")", res, n)

    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        self.dfs(0, 0, "", res, n)
        return res

from typing import List


class Solution:

    def cal(self, index: int, current: List[int], result: List[List[int]], nums: List[int]):
        if index == len(nums):
            result.append(current[:])  # Append a copy of the current subset
            return
        # Take the current element
        current.append(nums[index])
        self.cal(index + 1, current, result, nums)
        # Backtrack: don't take the current element
        current.pop()  
        self.cal(index + 1, current, result, nums)

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.cal(0, [], result, nums)
        return result





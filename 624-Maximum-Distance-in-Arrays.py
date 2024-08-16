from typing import List


class Solution:

    def maxDistance(self, arrays: List[List[int]]) -> int:
        min_num, max_num, max_distance = arrays[0][0], arrays[0][-1], 0
        for i in range(1, len(arrays)):
            max_distance = max(max_distance, abs(arrays[i][-1] - min_num), abs(max_num - arrays[i][0]))
            min_num = min(arrays[i][0], min_num)
            max_num = max(arrays[i][-1], max_num)
        return max_distance

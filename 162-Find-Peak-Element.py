from typing import List

def findPeakElement(nums: List[int]) -> int:
    n = len(nums)  # length of the nums

    #  defining base cases
    if n == 1:
        return 0
    elif nums[0] > nums[1]:
        return 0
    elif nums[n-1] > nums[n-2]:
        return n-1
    
    low, high = 0, n-2  # defining variable for the binary search
    while (low <= high):
        mid = (low + high) // 2
        if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:  # if we find mid > mid -1 and mid > mid + 1 then its is our peak element
            return mid
        elif nums[mid] > nums[mid - 1]:
            low = mid + 1
        else:
            high = mid - 1
    
    return -1









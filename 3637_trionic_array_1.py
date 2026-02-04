from math import inf
from typing import List


class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 4:
            return False

        i = 1

        # Phase 1: strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1
        if i == 1 or i == n:
            return False

        # Phase 2: strictly decreasing
        while i < n and nums[i] < nums[i - 1]:
            i += 1
        if i == n:
            return False

        # Phase 3: strictly increasing
        while i < n and nums[i] > nums[i - 1]:
            i += 1

        return i == n

print(Solution().isTrionic(nums=[8, 9, 4, 6, 1]))

from typing import List
from collections import Counter


class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        nums.sort()
        current = -(10**18)
        res = 0
        for n in nums:
            if current < n - k:
                current = n - k
            if current <= n + k:
                res += 1
                current += 1
        return res


print(Solution().maxDistinctElements([1, 2, 2, 3, 3, 4], 2))

from math import inf
from typing import List


class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return sum(nums)

        total = nums[0]

        rest = sorted(nums[1:])

        return total + sum(rest[0:2])


print("ans", Solution().minimumCost([1, 5, 1, 6]))
print("ans", Solution().minimumCost([10, 3, 1, 1]))
print(Solution().minimumCost([5, 3, 1, 2, 3, 6, 7, 9, 10, 22, 50, 2, 1, 2, 4, 5, 50]))

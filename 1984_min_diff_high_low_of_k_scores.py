from typing import List


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        if k == 1:
            return 0

        diff = float("inf")
        nums.sort()

        for i in range(0, len(nums) - k + 1):
            diff = min(diff, nums[i + k - 1] - nums[i])

        return diff


print(Solution().minimumDifference([9, 4, 1, 7], 2))

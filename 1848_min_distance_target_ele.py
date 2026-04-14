from typing import List


class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        ans = float("inf")
        for i, n in enumerate(nums):
            if target == n:
                ans = min(ans, abs(i - start))
        return ans


print(Solution().getMinDistance(nums=[1, 2, 3, 4, 5], target=5, start=3))

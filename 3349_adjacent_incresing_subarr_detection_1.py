from typing import List


class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        if k == 1:
            return True

        def check(sub):
            for i in range(len(sub) - 1):
                if sub[i] >= sub[i + 1]:
                    return False
            return True

        for i in range(n - 2 * k + 1):
            if check(nums[i : i + k]) and check(nums[i + k : i + 2 * k]):
                return True
        return False


print(Solution().hasIncreasingSubarrays([2, 5, 7, 8, 9, 2, 3, 4, 3, 1], 3))

print(Solution().hasIncreasingSubarrays([19, 4, 19, 6, 18], 2))  # true

print(Solution().hasIncreasingSubarrays([6, 13, -17, -20, 2], 2))  # false

print(Solution().hasIncreasingSubarrays([1, 2, 3, 4, 4, 4, 4, 5, 6, 7], 5))  # false

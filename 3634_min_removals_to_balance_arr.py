from typing import List


class Solution:
    def minRemoval(self, nums: List[int], k: int) -> int:
        if len(nums) == 1:
            return 0

        n = len(nums)

        nums.sort()

        low = 0
        longest_arr = 0

        for high in range(n):
            while nums[high] > nums[low] * k:
                l += 1

            longest_arr = max(longest_arr, high - low + 1)

        return n - longest_arr

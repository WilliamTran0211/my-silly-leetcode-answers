from collections import defaultdict
from math import e
from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        # ghép nums thành các cặp số. Trả về tổng lớn nhất của cặp số.
        # Sao cho tổng đó là nhỏ nhất trong tất cả các cách ghép.
        n = len(nums)
        nums.sort()

        res = -1
        for i in range(n - 1, (n // 2) - 1, -1):
            j = n - i - 1
            res = max(res, nums[i] + nums[j])

        return res



print(
    Solution().minPairSum1(
        nums=[9, 2, 10, 1, 10, 4, 8, 9, 7, 6, 8, 10, 8, 6, 5, 4, 3, 4, 2, 10]
    )
)  # 14

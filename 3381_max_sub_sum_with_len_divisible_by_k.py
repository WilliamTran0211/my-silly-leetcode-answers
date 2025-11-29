from platform import java_ver
from typing import List


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [float("inf")] * k
        prefix[0] = 0

        res = float("-inf")
        total = 0
        for i, n in enumerate(nums):
            total += n
            length = i + 1
            prefix_len = length % k

            res = max(res, total - prefix[prefix_len])
            prefix[prefix_len] = min(prefix[prefix_len], total)

        return res


print(Solution().maxSubarraySum([-5, 1, 2, -3, 4], 2))

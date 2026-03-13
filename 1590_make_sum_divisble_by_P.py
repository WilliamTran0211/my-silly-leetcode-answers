from collections import defaultdict
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p
        if remain == 0:
            return 0

        res = len(nums)

        check = {0: -1}
        curr_sum = 0
        for i, n in enumerate(nums):
            curr_sum = (curr_sum + n) % p
            prefix = (curr_sum - remain + p) % p
            if prefix in check:
                length = i - check[prefix]
                res = min(res, length)
            check[curr_sum] = i

        return -1 if res == len(nums) else res


print(Solution().minSubarray([6, 5, 2, 3], 9))

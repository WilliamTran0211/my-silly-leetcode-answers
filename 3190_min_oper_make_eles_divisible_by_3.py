from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            if n % 3 != 0:
                res += 1
        return res


print(Solution().minimumOperations([1, 2, 3, 15, 29, 41, 4]))

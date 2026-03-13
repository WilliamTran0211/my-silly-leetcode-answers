from typing import List


class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        n_set = set(nums)
        res = original

        while res in n_set:
            res *= 2

        return res


print(Solution().findFinalValue([5, 3, 6, 1, 12, 3, 6], 3))

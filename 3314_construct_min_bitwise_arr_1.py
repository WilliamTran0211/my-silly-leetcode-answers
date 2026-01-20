from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []

        for n in nums:
            candidate = []
            for i in range(n, 0, -1):
                if i | (i - 1) == n:
                    candidate.append(i - 1)
            if candidate:
                res.append(min(candidate))
            else:
                res.append(-1)

        return res


print(Solution().minBitwiseArray([2, 3, 5, 7]))  #  [-1,1,4,3]

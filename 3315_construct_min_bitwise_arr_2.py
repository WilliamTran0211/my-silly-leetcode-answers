from typing import List


class Solution:
    def minBitwiseArray(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if n % 2 == 0:
                res.append(-1)
            else:
                t = 0
                x = n
                while x & 1:
                    t += 1
                    x >>= 1
                res.append(n - (1 << (t - 1)))
        return res
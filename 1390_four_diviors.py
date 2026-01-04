from collections import defaultdict
from math import sqrt
from typing import List


class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        res = 0

        for n in nums:
            curr_fac = set()

            for i in range(1, int(sqrt(n)) + 1):
                if n % i == 0:
                    curr_fac.add(i)
                    curr_fac.add(n // i)
                if len(curr_fac) > 4:
                    break
            if len(curr_fac) == 4:
                res += sum(curr_fac)

        return res


print(Solution().sumFourDivisors(nums=[21, 4, 7]))

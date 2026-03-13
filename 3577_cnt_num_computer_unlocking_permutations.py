import math
from typing import List


class Solution:
    def countPermutations(self, complexity: List[int]) -> int:
        MOD = 10**9 + 7
        first_comp = complexity[0]
        for i in range(1, len(complexity)):
            if complexity[i] <= first_comp:
                return 0

        # (n-1)! = n!/n
        res = 0
        n = len(complexity)

        fac = 1
        for i in range(1, n + 1):
            fac *= i

        return (fac // n) % MOD


print(Solution().countPermutations([1, 2, 3]))

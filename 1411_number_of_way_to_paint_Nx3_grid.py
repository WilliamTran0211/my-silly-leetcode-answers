class Solution:
    def numOfWays(self, n: int) -> int:
        mod = 10**9 + 7
        dpA, dpB = 6, 6  # n = 1

        for i in range(2, n + 1):
            newA = (dpA * 3 + dpB * 2) % mod
            newB = (dpA * 2 + dpB * 2) % mod
            dpA, dpB = newA, newB

        return (dpA + dpB) % mod

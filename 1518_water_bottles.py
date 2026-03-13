class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        res = 0
        curr = 0
        while numBottles > 0:
            curr += 1
            numBottles -= 1
            if curr == numExchange:
                curr = 0
                numBottles += 1
            res += 1

        return res


print(Solution().numWaterBottles(9, 2))

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        res = numBottles

        empty = numBottles

        exchange = 0

        while empty > numExchange:
            empty -= numExchange
            exchange += 1
            numExchange += 1

            if empty < numExchange:
                if empty + exchange >= numExchange:
                    empty = (empty + exchange) - numExchange
                    exchange = 0
                    res += 1
            else:
                res += 1

        if exchange > 0 and exchange < numExchange:
            res += exchange

        return res


print(Solution().maxBottlesDrunk(7, 6))

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        # res = 0

        # n = low

        # while n <= high:
        #     if n % 2 == 0:
        #         n += 1
        #     else:
        #         res += 1
        #         n += 2

        # return res
        low = low + 1 if low % 2 == 0 else low
        high = high - 1 if high % 2 == 0 else high

        if low > high:
            return 0
        return ((high - low) // 2) + 1
    


print(Solution().countOdds(1, 99999))

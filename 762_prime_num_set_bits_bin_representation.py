class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        primes = set([2, 3, 5, 7, 11, 13, 17, 19, 23, 31])
        res = 0
        for n in range(left, right + 1):
            if n.bit_count() in primes:
                res += 1
        return res


print(Solution().countPrimeSetBits(10, 35))

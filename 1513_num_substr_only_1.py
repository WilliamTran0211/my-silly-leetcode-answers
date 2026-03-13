class Solution:
    def numSub(self, s: str) -> int:
        res = 0

        split_1 = s.split("0")

        for st in split_1:
            if st:
                n = len(st)
                res += n * (n + 1) / 2
        return res % (pow(10, 9) + 7)


print(Solution().numSub("0110111"))

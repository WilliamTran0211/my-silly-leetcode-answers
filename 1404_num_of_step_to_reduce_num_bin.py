class Solution:
    def numSteps(self, s: str) -> int:
        num = int(s, 2)

        res = 0

        if num == 1:
            return res

        while num != 1:
            if num % 2 == 0:
                num = num // 2
            else:
                num += 1

        return res


print(Solution().numSteps("1101"))

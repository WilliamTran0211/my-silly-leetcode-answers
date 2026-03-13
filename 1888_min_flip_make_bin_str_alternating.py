class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)

        alter_0 = "".join(str((0 + i) % 2) for i in range(n+n))
        alter_1 = "".join(str((1 + i) % 2) for i in range(n+n))

        s2 = s + s

        diff0 = 0
        diff1 = 0

        res = n

        l = 0
        for r in range(len(s2)):

            if s2[r] != alter_0[r]:
                diff0 += 1
            if s2[r] != alter_1[r]:
                diff1 += 1

            if r - l + 1 > n:
                if s2[l] != alter_0[l]:
                    diff0 -= 1
                if s2[l] != alter_1[l]:
                    diff1 -= 1

                l += 1

            if r - l + 1 == n:
                res = min(res, diff1, diff0)

        return res


print(Solution().minFlips("111000"))
print(Solution().minFlips("000111"))

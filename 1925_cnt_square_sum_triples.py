from collections import defaultdict


class Solution:
    def countTriples(self, n: int) -> int:
        cal_square = defaultdict(int)

        x = 3
        while x <= n:
            cal_square[x] = x**2
            x += 1

        res = 0
        check = set(cal_square.values())

        for _, n in cal_square.items():
            for _, m in cal_square.items():
                if (n + m) in check:
                    res += 1

        return res


print(Solution().countTriples(250))

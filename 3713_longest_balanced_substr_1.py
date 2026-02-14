from collections import Counter, defaultdict


class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                substr = s[i:j]
                count = Counter(substr)
                if len(set(count.values())) == 1:
                    res = max(res, len(substr))
        return res


print(Solution().longestBalanced("abbac"))

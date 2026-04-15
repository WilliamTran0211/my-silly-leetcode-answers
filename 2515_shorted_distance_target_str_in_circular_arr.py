from typing import List


class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:

        n = len(words)

        ans = float("inf")

        for i, w in enumerate(words):
            if target == w:
                dist_right = (i - startIndex + n) % n
                dist_left = (startIndex - i + n) % n

                ans = min(ans, min(dist_left, dist_right))

        return ans if ans != float("inf") else -1

    def closetTarget1(self, words, target, startIndex):
        n = len(words)

        positions = []
        for i in range(n):
            if words[i] == target:
                positions.append(i)

        if not positions:
            return -1

        res = float("inf")
        for i in positions:
            dist = min((i - startIndex) % n, (startIndex - i) % n)
            res = min(res, dist)

        return res


print(
    Solution().closestTarget(
        words=["hello", "i", "am", "leetcode", "hello"], target="hello", startIndex=1
    )
)

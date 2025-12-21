from typing import List


class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n = len(strs)
        m = len(strs[0])

        sorted_pairs = [False] * (n - 1)
        ans = 0

        for col in range(m):
            # 1. Check if this column breaks order
            bad = False
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] > strs[i + 1][col]:
                    bad = True
                    break

            if bad:
                ans += 1
                continue

            # 2. Update sorted_pairs
            for i in range(n - 1):
                if not sorted_pairs[i] and strs[i][col] < strs[i + 1][col]:
                    sorted_pairs[i] = True

            # 3. Early stop
            if all(sorted_pairs):
                break

        return ans

print(Solution().minDeletionSize(["abx", "agz", "bgc", "bfc"]))

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        if len(target) == 1:
            return target[0]

        count = target[0]

        for i in range(1, len(target)):
            if target[i] > target[i - 1]:
                count += target[i] - target[i - 1]

        return count


print(Solution().minNumberOperations([3, 1, 5, 4, 2]))

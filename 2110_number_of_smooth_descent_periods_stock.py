from typing import List


class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        res = 0

        current_des = []
        for i in range(len(prices)):
            if not current_des:
                current_des.append(prices[i])
            else:
                if current_des[-1] - prices[i] == 1:
                    current_des.append(prices[i])
                else:
                    n = len(current_des)
                    res += n * (n + 1) // 2
                    current_des.clear()
                    current_des.append(prices[i])
        if current_des:
            n = len(current_des)
            res += n * (n + 1) // 2
        return res


print(
    Solution().getDescentPeriods([12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 4, 3, 10, 9, 8, 7])
)
# print(Solution().getDescentPeriods([3, 2, 1, 4, 4, 5, 3, 2, 1, 5]))

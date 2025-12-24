"""
502. IPO
Suppose LeetCode will start its IPO soon. In order to sell a good price of its shares to Venture Capital, LeetCode would like to work on some projects to increase its capital before the IPO. Since it has limited resources, it can only finish at most k distinct projects before the IPO. Help LeetCode design the best way to maximize its total capital after finishing at most k distinct projects.

You are given n projects where the ith project has a pure profit profits[i] and a minimum capital of capital[i] is needed to start it.

Initially, you have w capital. When you finish a project, you will obtain its pure profit and the profit will be added to your total capital.

Pick a list of at most k distinct projects from given projects to maximize your final capital, and return the final maximized capital.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:

Input: k = 2, w = 0, profits = [1,2,3], capital = [0,1,1]
Output: 4
Explanation: Since your initial capital is 0, you can only start the project indexed 0.
After finishing it you will obtain profit 1 and your capital becomes 1.
With capital 1, you can either start the project indexed 1 or the project indexed 2.
Since you can choose at most 2 projects, you need to finish the project indexed 2 to get the maximum capital.
Therefore, output the final maximized capital, which is 0 + 1 + 3 = 4.
Example 2:

Input: k = 3, w = 0, profits = [1,2,3], capital = [0,1,2]
Output: 6

sử dụng 2 heap

1 max heap cho profit vì tổng profit cần có theo yêu cầu luôn là lớn nhất nên mỗi khi pop giá trị ta luôn cần giá trị lớn nhất của profits
1 min heap vì project chỉ có thể thực hiện khi tổng profits hiện tại của nó có thể đáp ứng (w phải lớn hơn hoặc bằng) capital của project.
complexity O(k * log n)
"""

from typing import List
import heapq


class Solution:
    def findMaximizedCapital(
        self, k: int, w: int, profits: List[int], capital: List[int]
    ) -> int:
        max_profit = []  # chỉ những project có thể thực hiện
        min_capital = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital)

        for i in range(k):
            while min_capital and min_capital[0][0] <= w:
                c, p = heapq.heappop(min_capital)
                heapq.heappush(max_profit, -1 * p)
            if not max_profit:
                break
            w += -1 * heapq.heappop(max_profit)

        return w


sol = Solution()
k = 2
w = 0
profits = [1, 2, 3]
capital = [0, 1, 1]
print("ans: ", sol.findMaximizedCapital(k, w, profits, capital))

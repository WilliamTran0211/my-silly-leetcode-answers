from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        stack = []
        ops = 0
        for x in nums:
            if x == 0:
                stack.clear()
                continue
            while stack and stack[-1] > x:
                stack.pop()
            if not stack or stack[-1] < x:
                ops += 1
                stack.append(x)
        return ops


#vì số 0 là số nhỏ nhất nên tránh subarr có số 0
print(Solution().minOperations([7, 2, 0, 4, 2]))

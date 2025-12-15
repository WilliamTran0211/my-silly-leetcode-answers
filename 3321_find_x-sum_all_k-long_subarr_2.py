from typing import List
from collections import Counter, defaultdict
from sortedcontainers import SortedList


class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        top = SortedList()
        remain = SortedList()
        freq = defaultdict(int)
        res = []
        curr_sum = 0

        def balance():
            nonlocal curr_sum
            if len(top) > x:
                f, n = top.pop(0)
                remain.add((f, n))
                curr_sum -= f * n
            if len(top) < x and remain:
                f, n = remain.pop(0)
                top.add((f, n))
                curr_sum += f * n

            if top and remain and top[0] < remain[-1]:
                f1, n1 = top.pop(0)
                f2, n2 = remain.pop()
                top.add((f2, n2))
                remain.add((f1, n1))
                curr_sum += f2 * n2 - f1 * n1

        def add(num):
            nonlocal curr_sum
            if num in freq:
                prev = (freq[num], num)
                if prev in top:
                    top.remove(prev)
                    curr_sum -= freq[num] * num
                else:
                    remain.remove(prev)

            freq[num] += 1
            top.add((freq[num], num))
            curr_sum += freq[num] * num
            balance()

        def remove(num):
            nonlocal curr_sum
            if num in freq:
                prev = (freq[num], num)
                if prev in top:
                    top.remove(prev)
                    curr_sum -= freq[num] * num
                else:
                    remain.remove(prev)

            freq[num] -= 1
            if freq[num] == 0:
                del freq[num]
            else:
                top.add((freq[num], num))
                curr_sum += freq[num] * num
            balance()

        for i in range(k):
            add(nums[i])

        res.append(curr_sum)
        for i in range(k, len(nums)):
            remove(nums[i - k])
            add(nums[i])
            res.append(curr_sum)

        return res


print(Solution().findXSum([3, 8, 7, 8, 7, 5], 2, 2))

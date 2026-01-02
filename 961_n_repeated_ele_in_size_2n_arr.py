from collections import defaultdict
from typing import Counter, List


class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        counter = Counter(nums)
        return max(counter, key=counter.get)

    def repeatedNTimes(self, nums: List[int]) -> int:
        times = len(nums) // 2
        count = defaultdict(int)

        for n in nums:
            count[n] += 1
            if count[n] == times:
                return n

    def repeatedNTimes(self, nums: List[int]) -> int:
        for i in range(len(nums) - 2):
            if nums[i] == nums[i + 1] or nums[i] == nums[i + 2]:
                return nums[i]

        return nums[-1]

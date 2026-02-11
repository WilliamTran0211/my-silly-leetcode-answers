from collections import defaultdict
from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)
        for l in range(0, n - 1):

            even_freq = defaultdict(int)
            odd_freq = defaultdict(int)

            dist_even = 0
            dist_odd = 0

            for r in range(l, n - 1):
                x = nums[r]

                if x % 2 == 0:
                    even_freq[x] += 1
                    if even_freq[x] == 1:
                        dist_even += 1
                else:
                    odd_freq[x] += 1
                    if odd_freq[x] == 1:
                        dist_odd += 1

                if dist_even == dist_odd:
                    ans = max(ans, r - l + 1)
        return ans

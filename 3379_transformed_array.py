from typing import List


class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        new_array = []
        for i in range(n):
            next_idx = nums[i]

            if next_idx == 0:
                new_array.append(0)
            else:

                if next_idx > 0:
                    if next_idx + i < n:
                        new_array.append(nums[next_idx + i])
                    else:
                        idx = i
                        cnt = 0
                        while cnt < next_idx:
                            idx = 0 if idx == n - 1 else idx + 1
                            cnt += 1
                        new_array.append(nums[idx])
                else:
                    idx = i
                    cnt = 0
                    while cnt < abs(next_idx):
                        idx = n - 1 if idx == 0 else idx - 1
                        cnt += 1

                    new_array.append(nums[idx])
        return new_array


print(Solution().constructTransformedArray([35, -5, 1, 1]))  # [1,35,1,35]

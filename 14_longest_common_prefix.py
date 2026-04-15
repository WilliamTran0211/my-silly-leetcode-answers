from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort(key=lambda x: len(x))
        prefix = strs[0]
        for i in range(1, len(strs)):
            while not strs[i].startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))  # fl
print(Solution().longestCommonPrefix(["dogcar", "racecar", "car"]))  # ""

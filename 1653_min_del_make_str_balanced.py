class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        cnt_B = 0
        for c in s:
            if c == "b":
                cnt_B += 1
            else:
                dp = min(dp + 1, cnt_B)

        return dp


print(Solution().minimumDeletions("baababbaabbaaabaabbabbbabaaaaaabaabababaaababbb"))

from typing import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        if len(s) == 3:
            return 1 if s[0] == s[-1] else 0

        res = 0

        formed = set()

        for i in range(len(s)):
            char = s[i]
            check_right = len(s) - 1
            if char not in formed:
                while char != s[check_right]:
                    check_right -= 1
                    if check_right <= i:
                        break

                check_sub = set(s[i + 1 : check_right])
                res += len(check_sub)
                formed.add(char)

        return res


print(Solution().countPalindromicSubsequence("narisoerjteokvhfupilrnuytrhrqcygiudbzptlxosjkdrxwx"))

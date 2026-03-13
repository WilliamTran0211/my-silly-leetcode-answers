from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = []
        w_current = ""
        for i in range(len(words)):
            if not res:
                res.append(words[i])
                w_current = "".join(sorted(words[i]))
            else:
                w_check = "".join(sorted(words[i]))
                if w_check != w_current:
                    w_current = w_check
                    res.append(words[i])

        return res


print(Solution().removeAnagrams(["abba", "baba", "bbaa", "cd", "cd", "baba"]))

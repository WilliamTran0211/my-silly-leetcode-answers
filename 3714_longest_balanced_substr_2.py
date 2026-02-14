class Solution:
    def longestBalanced(self, s: str) -> int:
        cnt_a, cnt_b, cnt_c = 0, 0, 0

        ans = 0

        check = {(0, 0): -1}

        same = 0
        prev = ""

        for i, ch in enumerate(s):


            if ch == prev:
                same += 1
            else:
                same = 1
                prev = ch

            ans = max(ans, same)

            if ch == "a":
                cnt_a += 1
            elif ch == "b":
                cnt_b += 1
            else:
                cnt_c += 1

            key = (cnt_b - cnt_a, cnt_c - cnt_a)

            if key in check:
                ans = max(ans, i - check[key])
            else:
                check[key] = i

        return ans

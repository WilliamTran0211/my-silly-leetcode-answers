class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)

        next_zero = [n] * n
        for i in range(n - 2, -1, -1):
            if s[i + 1] == "0":
                next_zero[i] = i + 1
            else:
                next_zero[i] = next_zero[i + 1]

        res = 0
        for l in range(n):
            zeros = 1 if s[l] == "0" else 0
            r = l

            while zeros * zeros <= n:
                nxt_z = next_zero[r] 
                ones = (nxt_z - l) - zeros

                if ones >= zeros * zeros:
                    res += min(nxt_z - r, ones - zeros * zeros + 1)
                r = nxt_z
                zeros += 1
                if r == n:
                    break
        return res

class Solution:
    def maxPartitionsAfterOperations(self, s: str, k: int) -> int:
        n = len(s)
        if k == 26:
            return 1

        left = [[0, 0] for _ in range(n + 1)]
        count, mask = 1, 0

        for i in range(n):
            num = ord(s[i]) - ord("a")
            if (mask >> num) & 1:
                left[i + 1] = [count, mask]
                continue

            if bin(mask).count("1") == k:
                count += 1
                mask = 1 << num
            else:
                mask |= 1 << num
            left[i + 1] = [count, mask]

        right = [[0, 0] for _ in range(n + 1)]
        count, mask = 1, 0
        for i in range(n - 1, -1, -1):
            num = ord(s[i]) - ord("a")
            if (mask >> num) & 1:
                right[i] = [count, mask]
                continue

            if bin(mask).count("1") == k:
                count += 1
                mask = 1 << num
            else:
                mask |= 1 << num
            right[i] = [count, mask]

        res = right[0][0]

        for i in range(n):
            for j in range(26):
                c = chr(ord("a") + j)
                if s[i] == c:
                    continue

                left_cnt, left_mask = (left[i][0] - 1, left[i][1]) if i > 0 else (0, 0)
                right_cnt, right_mask = (
                    (right[i + 1][0], right[i + 1][1]) if i < n - 1 else (0, 0)
                )

                new_mask = left_mask | (1 << j) | right_mask

                if bin(new_mask).count("1") <= k:
                    res = max(res, left_cnt + 1 + right_cnt)
                else:
                    res = max(res, left_cnt + 2 + right_cnt)

        return res


print(Solution().maxPartitionsAfterOperations("accca", 2))

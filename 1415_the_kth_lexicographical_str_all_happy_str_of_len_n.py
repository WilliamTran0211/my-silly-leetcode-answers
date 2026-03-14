class Solution:
    def getHappyString(self, n: int, k: int) -> str:

        limit = 3 * 2 ** (n - 1)

        if k > limit:
            return ""

        results = ""
        chars = ["a", "b", "c"]

        for p in range(n):
            for ch in chars:
                if p > 0 and ch == results[-1]:
                    continue
                count = 2 ** (n - p - 1)

                if k > count:
                    k = k - count
                else:
                    results += ch
                    break

        return results

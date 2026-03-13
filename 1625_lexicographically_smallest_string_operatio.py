class Solution:
    def findLexSmallestString(self, s: str, a: int, b: int) -> str:

        visit = set()

        def add(s):
            lst = list(s)
            for i in range(1, len(lst), 2):
                lst[i] = str((int(lst[i]) + a) % 10)
            return "".join(lst)

        def rotate(s):
            return s[len(s) - b :] + s[0 : len(s) - b]

        self.res = s

        def dfs(s, visit):
            if s in visit:
                return

            visit.add(s)

            if s < self.res:
                self.res = s

            s1 = add(s)
            dfs(s1, visit)

            s2 = rotate(s)
            dfs(s2, visit)

        dfs(s, visit)
        return self.res


print(Solution().findLexSmallestString("74", 5, 1))  # "00553311"

# print(Solution().findLexSmallestString("43987654", 7, 3))  # "00553311"

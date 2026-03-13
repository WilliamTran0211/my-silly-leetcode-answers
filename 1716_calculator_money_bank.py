class Solution:
    def totalMoney(self, n: int) -> int:
        res =0
        if n <=7:
            res = (n * (n+1)) //2
        else:
            start = 1
            end = 7
            while n > 0:
                res += ( (end-start +1) / 2) * (start + end)
                start += 1
                n -= 7 
                if n > 7:
                    end += 1
                else:
                    end = start + n - 1

        return int(res)


print(Solution().totalMoney(4))

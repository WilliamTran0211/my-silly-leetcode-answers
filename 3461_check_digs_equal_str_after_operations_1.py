class Solution:
    def hasSameDigits(self, s: str) -> bool:
        nums = list(s)
        temp_nums = []
        while len(nums) > 2:
            for i in range(len(nums) - 1):
                cal = (int(nums[i]) + int(nums[i + 1])) % 10
                temp_nums.append(cal)
            nums = temp_nums.copy()
            temp_nums.clear()

        return True if len(set(nums)) == 1 else False


print(Solution().hasSameDigits("3902"))
print(Solution().hasSameDigits("4867716181911413979960155821878"))

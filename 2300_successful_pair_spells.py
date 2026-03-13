from typing import List


class Solution:
    def successfulPairs(
        self, spells: List[int], potions: List[int], success: int
    ) -> List[int]:
        """
        Trả về mảng giá trị có số lượng phần tử bằng với mảng spells
        Mỗi phần tử trong mảng là số kết quả  mà nhân 1 phần tử của spells với tất cả phần tử của mảng potions mà có giá trị lớn hơn hoặc bằng success

        """
        res = []
        p = len(potions)
        potions.sort()
        for i in range(len(spells)):
            spell = spells[i]
            flag = (success + spell - 1) // spell
            l, r = 0, p - 1
            pos = p  # mặc định là không có potion đủ mạnh

            # binary search thủ công
            while l <= r:
                mid = (l + r) // 2
                if potions[mid] >= flag:
                    pos = mid
                    r = mid - 1
                else:
                    l = mid + 1

            res.append(p - pos)
        return res


print(Solution().successfulPairs([3, 1, 2], [8, 5, 8], 16))

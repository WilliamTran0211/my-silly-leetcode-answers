from typing import List


class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        # chạy n máy tính cùng lúc, 1 phút chay bằng 1 phút dùng pin, nếu 1 máy không có pin thay thế thì trả về số phút đã chạy lớn nhất.
        # điều kiện thì tổng của batteries(tức là tối đa pin có thể cung cấp) sẽ >= n máy tính * T thời gian chạy.
        # vì 1 máy tính chạy tốn 1 phút. n máy tính chạy tốn n phút.
        # vậy thời gian n máy chay trong T phút phải nhỏ hơn tổng thời gian mà pin có thể dùng

        low = 1
        high = sum(batteries) // n

        while low <= high:
            # T Phút
            t = (high + low) // 2

            curr_bat = 0
            for b in batteries:
                curr_bat += min(b, t)

            if curr_bat >= n * t:
                low = t + 1
            else:
                high = t - 1
        return high


print(Solution().maxRunTime(2, [3, 3, 3]))

from collections import defaultdict
from typing import List


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n = len(events)
        events.sort(key=lambda item: item[0])

        dp = defaultdict(int)
        dp[n - 1] = events[n - 1][2]

        for i in range(n - 2, -1, -1):
            dp[i] = max(dp[i + 1], events[i][2])

        res = 0

        def find_next_time(curr_i, last_end_time):
            # run binary here
            low = curr_i + 1
            high = n - 1
            # next time must come after last end time
            need_time = last_end_time + 1
            find_time_idx = -1
            while low <= high:
                mid = low + (high - low) // 2
                if events[mid][0] >= need_time:
                    find_time_idx = mid
                    high = mid - 1
                else:
                    low = mid + 1
            return find_time_idx

        for i in range(n):
            time_end = events[i][1]
            next_event_idx = find_next_time(i, time_end)
            res = max(
                res,
                (
                    events[i][2] + dp[next_event_idx]
                    if next_event_idx != -1
                    else events[i][2]
                ),
            )

        return res

        # for i in range(n - 1):
        #     dp[i] = max(dp[i + 1], events[i][2])
        #     cur_val = events[i][2]
        #     print("i ", i, events[i], "curr ", cur_val)

        #     for j in range(i + 1, n):
        #         if events[j][0] > events[i][1]:
        #             print("   j ", j, events[j])
        #             cur_val = max(cur_val, dp[i] + events[j][2])
        #             print("total", cur_val)
        #     dp[i] = cur_val
        # print(dp)
        # return max(dp.values())


print(Solution().maxTwoEvents([[1, 5, 3], [1, 5, 1], [6, 6, 5]]))

from collections import defaultdict
from multiprocessing import heap
from typing import List
import heapq


class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        sorted_meetings = sorted(meetings, key=lambda items: items[0])

        count = [0] * n

        available_rooms = []
        in_use = []

        for room in range(n):
            heapq.heappush(available_rooms, room)

        for meeting in sorted_meetings:
            start, end = meeting[0], meeting[1]

            while in_use and in_use[0][0] <= start:
                end_time, room = heapq.heappop(in_use)
                heapq.heappush(available_rooms, room)

            if available_rooms:
                new_room = heapq.heappop(available_rooms)
                meeting_info = (end, new_room)
                heapq.heappush(in_use, meeting_info)
                count[new_room] += 1
            else:
                # process delay
                end_time, room = heapq.heappop(in_use)
                duration = end - start

                new_end = end_time + duration

                heapq.heappush(in_use, (new_end, room))
                count[room] += 1

        max_hold_meeting = max(count)

        return count.index(max_hold_meeting)


print(Solution().mostBooked(n=3, meetings=[[1, 20], [2, 10], [3, 5], [4, 9], [6, 8]]))

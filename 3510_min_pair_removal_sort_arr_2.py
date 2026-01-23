from typing import List
import heapq


class Solution:
    # def minimumPairRemoval(self, nums: List[int]) -> int:

    #     class Node:
    #         def __init__(self, val, idx):
    #             self.val = val
    #             self.idx = idx
    #             self.prev = None
    #             self.next = None
    #             self.alive = True

    #     # create doubly linked list
    #     def create_dll(arr):
    #         head = Node(arr[0], 0)
    #         curr = head
    #         for idx, num in enumerate(arr[1:]):
    #             new_node = Node(num, idx)
    #             curr.next = new_node
    #             new_node.prev = curr
    #             curr = new_node
    #         return head

    #     head = create_dll(nums)
    #     bad_cnt = 0
    #     heap = []
    #     curr_head = head
    #     while curr_head and curr_head.next:
    #         if curr_head.val > curr_head.next.val:
    #             bad_cnt += 1
    #         sum_next = curr_head.val + curr_head.next.val
    #         heapq.heappush(heap, (sum_next, curr_head.idx, curr_head))
    #         curr_head = curr_head.next

    #     count_op = 0

    #     while bad_cnt > 0:
    #         _, _, node = None, None, None

    #         while True:
    #             _, _, node = heapq.heappop(heap)
    #             if not node.alive:
    #                 continue
    #             if node.next is None:
    #                 continue
    #             if not node.next.alive:
    #                 continue
    #             break

    #         v = node.next
    #         prev = node.prev
    #         next = v.next

    #         # if prev is not None and prev.val > node.val:
    #         #     bad_cnt -= 1
    #         # if node.val > v.val:
    #         #     bad_cnt -= 1
    #         # if next is not None and v.val > next.val:
    #         #     bad_cnt -= 1

    #         if prev is not None and next is not None and prev.val > next.val:
    #             bad_cnt += 1
    #         new_val = node.val + v.val

    #         new_node = Node(new_val, next.idx if next is not None else node.idx + 1)
    #         new_node.prev = prev
    #         new_node.next = next

    #         if prev is not None:
    #             prev.next = new_node
    #         else:
    #             head = new_node

    #         if next is not None:
    #             next.prev = new_node

    #         node.alive = False
    #         v.alive = False

    #         if prev is not None and next is not None and prev.val > next.val:
    #             bad_cnt -= 1

    #         # if prev is not None and prev.val > new_node.val:
    #         #     bad_cnt += 1
    #         # if next is not None and new_node.val > next.val:
    #         #     bad_cnt += 1

    #         if prev is not None:
    #             heapq.heappush(heap, (prev.val + new_node.val, prev.idx, prev))

    #         if next is not None:
    #             heapq.heappush(heap, (new_node.val + next.val, new_node.idx, new_node))

    #         count_op += 1

    #     return count_op

    def minimumPairRemoval(self, nums: List[int]) -> int:
        class Node:
            def __init__(self, val, idx):
                self.val = val
                self.idx = idx
                self.prev = None
                self.next = None
                self.alive = True

            def __lt__(self, other):
                # So sánh based on idx khi cần
                return self.idx < other.idx

        # create doubly linked list
        def create_dll(arr):
            head = Node(arr[0], 0)
            curr = head
            for i in range(1, len(arr)):
                new_node = Node(arr[i], i)
                curr.next = new_node
                new_node.prev = curr
                curr = new_node
            return head

        head = create_dll(nums)
        bad_cnt = 0
        heap = []

        # Đếm vi phạm và khởi tạo heap
        curr = head
        idx = 0
        while curr and curr.next:
            if curr.val > curr.next.val:
                bad_cnt += 1
            heapq.heappush(heap, (curr.val + curr.next.val, idx, curr, curr.next))
            curr = curr.next
            idx += 1

        count_op = 0

        while bad_cnt > 0 and heap:
            # Tìm pair hợp lệ
            while True:
                if not heap:
                    return count_op
                _, _, left, right = heapq.heappop(heap)
                if left.alive and right.alive and left.next == right:
                    break

            # Kiểm tra vi phạm giữa prev và next (nếu có)
            prev = left.prev
            next = right.next

            if prev and next and prev.val > next.val:
                bad_cnt += 1  # Vi phạm tiềm ẩn sẽ xuất hiện

            # Xóa vi phạm cũ
            if prev and prev.val > left.val:
                bad_cnt -= 1
            if left.val > right.val:
                bad_cnt -= 1
            if next and right.val > next.val:
                bad_cnt -= 1

            # Xóa vi phạm giữa prev và next (nếu có)
            if prev and next and prev.val > next.val:
                bad_cnt -= 1

            # Tạo node mới
            new_val = left.val + right.val
            new_node = Node(new_val, left.idx)
            new_node.prev = prev
            new_node.next = next

            if prev:
                prev.next = new_node
            else:
                head = new_node

            if next:
                next.prev = new_node

            left.alive = False
            right.alive = False

            # Thêm vi phạm mới
            if prev and prev.val > new_val:
                bad_cnt += 1
            if next and new_val > next.val:
                bad_cnt += 1

            # Thêm pair mới vào heap
            if prev:
                heapq.heappush(heap, (prev.val + new_val, prev.idx, prev, new_node))
            if next:
                heapq.heappush(heap, (new_val + next.val, new_node.idx, new_node, next))

            count_op += 1

        return count_op


print(Solution().minimumPairRemoval([1, 1, 4, 4, 2, -4, -1]))  # 5

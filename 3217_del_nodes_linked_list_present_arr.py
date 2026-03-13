from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return "val: " + str(self.val) + " | next: " + str(self.next)


def create_linked_list(my_list):
    head = None
    for idx, item in enumerate(my_list):
        new_node = ListNode(item)
        if head is None:
            head = new_node
        else:
            current = head
            while current.next:
                current = current.next
            current.next = new_node
    return head


class Solution:
    def modifiedList(
        self, nums: List[int], head: Optional[ListNode]
    ) -> Optional[ListNode]:
        del_set = set(nums)
        #create a dummy for ref to the head of linkedList and to make sure that 
        #if the val of the first item and the last item surely remove when they are on the nums list s
        dummy = ListNode(0, head)
        curr = dummy
        while curr.next:
            if curr.next.val in del_set:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return dummy.next


list_node = create_linked_list([2, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1])
print(Solution().modifiedList([1], list_node))

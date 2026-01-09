from typing import List, Optional
from collections import deque


# ===== Linked List =====
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"{self.val}->{self.next}"


# ===== Binary Tree =====
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return f"<{self.val}, {self.left}, {self.right}>"  # Py 3.6


# ===== Graph / N-ary =====
class Node:
    def __init__(
        self,
        val: Optional[int] = None,
        children: Optional[List["Node"]] = None,
        neighbors: Optional[List["Node"]] = None,
    ):
        self.val = val
        self.children = children if children is not None else []
        self.neighbors = neighbors if neighbors is not None else []

    def __str__(self):
        # Chỉ liệt kê giá trị của các node láng giềng để tránh vòng lặp vô hạn
        neighbor_vals = [n.val for n in self.neighbors] if self.neighbors else []
        child_vals = [c.val for c in self.children] if self.children else []

        res = f"Node({self.val})"
        if neighbor_vals:
            res += f" -> Neighbors: {neighbor_vals}"
        if child_vals:
            res += f" -> Children: {child_vals}"
        return res


class utils:
    @staticmethod
    def listToLinkedList(arr: List):
        dummy = ListNode(0)
        ptr = dummy
        for x in arr:
            ptr.next = ListNode(x)
            ptr = ptr.next
        return dummy.next

    @staticmethod
    def linked_list_to_array(head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    @staticmethod
    def grow_a_tree_from_list(root_lst: List[int]) -> Optional[TreeNode]:
        # this is better because it dont create node with None value
        root_node = TreeNode(val=root_lst[0])
        nodes = [root_node]
        for i, val in enumerate(root_lst[1:]):
            if val is None:
                continue
            parent_node = nodes[i // 2]
            is_left = (i % 2) == 0
            node = TreeNode(val=val)
            if is_left:
                parent_node.left = node
            else:
                parent_node.right = node
            nodes.append(node)

        return root_node

    @staticmethod
    def build_binary_tree(arr: List[int]) -> Optional[TreeNode]:
        if not arr or arr[0] is None:
            return None

        root = TreeNode(arr[0])
        q = deque([root])
        i = 1

        while q and i < len(arr):
            node = q.popleft()

            if i < len(arr) and arr[i] is not None:
                node.left = TreeNode(arr[i])
                q.append(node.left)
            i += 1

            if i < len(arr) and arr[i] is not None:
                node.right = TreeNode(arr[i])
                q.append(node.right)
            i += 1

        return root

    @staticmethod
    def build_graph(adj):
        if not adj:
            return None

        nodes = {i + 1: Node(i + 1) for i in range(len(adj))}

        for i, neighbors in enumerate(adj):
            nodes[i + 1].neighbors = [nodes[n] for n in neighbors]

        return nodes[1]

    @staticmethod
    def build_nary_tree(arr):
        if not arr:
            return None

        root = Node(arr[0], children=[])
        q = deque([root])
        i = 2  # skip root and first None

        while q and i < len(arr):
            parent = q.popleft()

            while i < len(arr) and arr[i] is not None:
                child = Node(arr[i], children=[])
                parent.children.append(child)
                q.append(child)
                i += 1
            i += 1  # skip None

        return root

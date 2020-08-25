# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
Be careful:
    to do multiple assignment in one line, please be aware of the sequence.
    node.next first, then other:
        variables to be changed first, then other variables
"""
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return head

        fast = head
        slow = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        prev, cur = None, slow
        while cur:
            cur.next, prev, cur = prev, cur, cur.next

        first = head
        second = prev

        while second.next:
            first.next, first = second, first.next
            second.next, second = first, second.next
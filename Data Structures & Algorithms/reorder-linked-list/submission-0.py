# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        secondL = slow.next
        slow.next = None

        prev = None
        while secondL:
            tmp = secondL.next
            secondL.next = prev
            prev = secondL
            secondL = tmp

        firstL = head
        secondL = prev

        while firstL and secondL:
            ftmp = firstL.next
            stmp = secondL.next

            firstL.next = secondL
            secondL.next = ftmp

            secondL = stmp
            firstL = ftmp

        
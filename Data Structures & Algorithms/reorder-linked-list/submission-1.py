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
        
        second = slow.next
        slow.next = None
        
        prev = None
        while second:
            tmp = second.next 
            second.next = prev
            prev = second 
            second = tmp

        second = prev
        first = head

        while first and second:
            tmpf = first.next
            tmps = second.next

            first.next = second
            second.next = tmpf

            first = tmpf
            second = tmps

        
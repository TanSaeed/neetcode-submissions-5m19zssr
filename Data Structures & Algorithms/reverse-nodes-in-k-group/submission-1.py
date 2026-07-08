# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        gprev = dummy

        while True:
            kth = self.getKth(gprev,k)
            if not kth:
                break
            
            gnext = kth.next

            prev = kth.next
            cur = gprev.next

            while cur != gnext:
                tmp = cur.next
                cur.next = prev
                prev = cur
                cur = tmp

            tmp = gprev.next
            gprev.next = kth
            gprev = tmp

        return dummy.next




    def getKth(self, node, k):
        while node and k > 0:
            node = node.next
            k -= 1
        return node







    




        
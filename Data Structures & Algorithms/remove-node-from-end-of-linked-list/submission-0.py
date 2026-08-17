# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head:
            return None

        head = self.reverseList(head)
        prev, curr = None, head

        while n > 1:
            prev = curr
            curr = curr.next
            n -= 1

        if not prev:
            head = head.next

        else:
            prev.next = curr.next

        return self.reverseList(head)

        
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
            if not head:
                return None

            prev, curr = None, head
            tmp = None

            while curr:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            return prev


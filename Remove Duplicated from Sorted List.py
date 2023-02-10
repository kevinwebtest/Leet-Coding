# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        distinct=set()
        root = previous = head
        while head:
            if head.val in distinct:
                previous.next = head.next
            else:
                distinct.add(head.val)
                previous = head
            head = head.next
        return root
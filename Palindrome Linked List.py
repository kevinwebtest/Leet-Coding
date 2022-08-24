# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        toList = []
        toList = self.linkedToList(head, toList)
        half = len(toList)//2
        for i in range(half):
            if toList[i] == toList[-i-1]:
                continue
            else:
                return False
        return True
        
        
    def linkedToList(self, head, toList):
        if not head:
            return head
        toList.append(head.val)
        head.next = self.linkedToList(head.next, toList)
        return toList

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast, prev = head, head, None
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        prev, slow, prev.next = slow, slow.next, None
        while slow:
            slow.next, prev, slow = prev, slow, slow.next
        fast, slow = head, prev
        while slow:
            if fast.val != slow.val: return False
            fast, slow = fast.next, slow.next
        return True

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head.next
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        new = slow.next 
        slow.next = None
        prev = None
        while new:
            temp = new.next
            new.next = prev
            prev = new 
            new = temp
        
        second = prev
        first = head
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second 
            second.next = temp1
            first = temp1
            second = temp2 
        

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        counter1 = 0
        counter2 = 0
        cur = head
        pointer = head
        while pointer:
            if counter1+n == counter2-1:
                counter1 += 1 
                
                if pointer.next == None:
                    cur = cur.next
                    prev = cur
                else:
                    cur = cur.next
            pointer = pointer.next
            counter2 += 1
            print(counter1, counter2)
        if counter2 == n:
            return head.next
        elif counter2 == n+1:
            head.next = head.next.next
        elif n >1:
            prev.next = cur.next.next
        elif n == 1 and head.next != None:
            cur.next  = None

        else:
            return None
        return head
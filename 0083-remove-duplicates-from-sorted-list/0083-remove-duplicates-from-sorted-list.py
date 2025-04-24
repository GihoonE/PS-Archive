# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ret = head
        if not head:
            return ret
        while head.next:
            cur = head
            com = head.next
            if cur.val == com.val:
                if com.next:
                    cur.next = com.next
                else:
                    cur.next = None
            else:                
                if cur.next:
                    head = cur.next
                else:
                    break
        return ret
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first = True
        ret = None
        while head is not None:
            n1 = head
            head = head.next
            if head is not None: #swap 2 nodes
                n2 = head
                n1.val,n2.val = n2.val,n1.val   
                head = head.next
                if first:
                    ret = ListNode(n1.val,None)
                    ans = ret
                    first = not first
                else:
                    ans.next = ListNode(n1.val,None)
                    ans = ans.next
                ans.next = ListNode(n2.val,None)
                ans = ans.next
            else: #no need for swaps
                if first:
                    ret = ListNode(n1.val,None)
                    first = not first
                else:
                    ans.next = ListNode(n1.val, None)
        return ret
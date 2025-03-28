# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = 0
        n2 = 0
        ind = 0
        while l1.next != None:
            n1 += 10**ind*l1.val
            l1 = l1.next
            ind += 1
        n1 += 10**ind*l1.val
        ind = 0
        while l2.next != None:
            n2 += 10**ind*l2.val
            l2 = l2.next
            ind += 1
        n2 += 10**ind*l2.val 
        sum = n1+n2
        ans = ListNode(0,None)
        ret = ans
        while sum != 0:
            digit = sum%10
            ret.val=digit
            sum = sum//10
            if sum == 0:
                break
            ret.next = ListNode(0,None)
            ret = ret.next
        return ans
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:  
        num1, num2, i = 0, 0, 1
        
        while l1:
            num1 += (l1.val * i)
            i *= 10
            l1 = l1.next
        
        i = 1
        while l2:
            num2 += (l2.val * i)
            i *= 10
            l2 = l2.next
        summation = str(num1 + num2)
        
        node = ListNode(int(summation[-1]))
        result = node
        for i in range(len(summation)-2, -1, -1):
            node.next = ListNode(int(summation[i]))
            node = node.next

        return result
            
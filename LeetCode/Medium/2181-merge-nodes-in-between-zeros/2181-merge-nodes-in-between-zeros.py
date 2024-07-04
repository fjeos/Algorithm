# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        head = head.next
        summ = 0
        node = ListNode()
        result = node
        
        while head:
            if head.val == 0:
                node.val = summ
                summ = 0
                if head.next != None:
                    node.next = ListNode()
                node = node.next
            else: 
                summ += head.val
            head = head.next
            
        return result
            
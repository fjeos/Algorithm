# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        nodes = [head.val]
        next_node = head.next
        
        while next_node is not None:
            nodes.append(next_node.val)
            next_node = next_node.next
            
        for i in range(len(nodes)):
            if nodes[i] != nodes[-i-1]:
                return False
        return True
    
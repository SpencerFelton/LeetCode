# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:

        num_1 = []
        num_2 = []
        while l1 != None:
            num_1.insert(0, l1.val)
            l1 = l1.next
        while l2!= None:
            num_2.insert(0,l2.val)
            l2 = l2.next
        num_1 = [str(x) for x in num_1]
        num_1 = int(''.join(num_1))

        num_2 = [str(y) for y in num_2]
        num_2 = int(''.join(num_2))

        ans = num_1 + num_2

        ans = str(ans)
        ans = list(ans)

        ans = [int(x) for x in ans]
        current_node = ListNode()

        for x in range(0,len(ans)):
            if(x == 0):
                node = ListNode(ans[0], None)
                current_node = node
                if(len(ans) == 1):
                    return node
            elif(x > 0 and x <len(ans)-1):
                node = ListNode(ans[x],current_node)
                current_node = node
                continue
            elif(x == len(ans)-1):
                linked_list = ListNode(ans[x], current_node)
                return linked_list

'''
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
Example 1:

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10

Example 2:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
'''

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        l1 = []
        sum = 0
        while head:
            l1.append(head.val)
            head = head.next
        length = len(l1) -1
        for i, j in enumerate(l1):
            sum += j*(2**(length-i))
        return sum

    def another_logic(self, head: ListNode) -> int:
        ans = 0
        while head:
            ans = ans*2 + head.val
            head = head.next
        return ans

def toListNode(numbers):
    # Generate list from the input
    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

if __name__=='__main__':
    sol = Solution()
    ans1 = sol.getDecimalValue(head=toListNode([1,0,1]))
    assert (ans1 == 5), 'wrong'

    ans2 = sol.getDecimalValue(head=toListNode([1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]))
    assert(ans2 == 18880), 'wrong'





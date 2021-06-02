# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def get_num(l: ListNode) -> str:
            num = str(l.val)
            while l.next is not None:
                l = l.next
                num += str(l.val)
            return num

        num1 = get_num(l1)
        num2 = get_num(l2)
        num_sum = str(int(num1) + int(num2))

        def create_list(i, num_l):
            if i == len(num_sum):
                return

            if i < len(num_sum):
                temp = ListNode(int(num_sum[i]))
                num_l.next = temp
                i += 1
                return create_list(i, temp)
        root = ListNode(int(num_sum[0]))
        create_list(1, root)

        return root


if __name__ == '__main__':
    sol = Solution()
    # Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
    l1 = ListNode(7)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)
    l1.next.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l3 = sol.addTwoNumbers(l1, l2)
    print(l3.val)
    while l3.next:
        l3 = l3.next
        print(l3.val)
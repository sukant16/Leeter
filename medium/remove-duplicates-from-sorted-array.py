'''

Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Approach:

1. Use Deque
2. iterator over the length, check if first element is lesser than the second,
if yes:
    push it to the right
if same:
    pop it from deque
continue till i < len
'''


from collections import deque
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums = deque(nums)
        n = len(nums)
        i = 0
        while i < n:
            if nums[0] == nums[1]:
                nums.popleft()
            else:
                nums.append(nums.popleft())
            i += 1
        print(nums)
        return len(nums)

    def list_sol(self, nums):
        n = len(nums)
        current = 0
        ix = 1

        for i in range(1, n-1):
            if nums[ix] != nums[i+1]:
                nums[ix], nums[i+1] = nums[i+1], nums[i]
                ix


if __name__ == '__main__':
    sol = Solution()
    print(sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
    print(sol.removeDuplicates([1,1,2]))
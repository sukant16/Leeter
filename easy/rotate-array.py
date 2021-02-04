from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(k):
            new_nums = [nums[n-1]] + nums[:(n-1)]
            nums[:] = new_nums
            print(nums)


if __name__ == '__main__':
    sol = Solution()
    sol.rotate([1, 2], 3)
    sol.rotate([1,2,3,4,5,6,7], 4)
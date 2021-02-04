from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            residual = target - nums[i]
            if residual in nums[(i+1):]:
                return [i, nums[(i+1):].index(residual) + i+1]

    def using_hashmap(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for idx, num in enumerate(nums):
            res = target - num
            if res in d:
                return [d[res], idx]
            else:
                d[num] = idx


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums = [2,7,11,15], target = 9))
    print(sol.twoSum(nums = [3,3], target = 6))


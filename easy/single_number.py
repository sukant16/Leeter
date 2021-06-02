from typing import  List
from collections import  defaultdict


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        Time complexity O(n) and space complexity O(n)
        """
        # n = len(nums)
        # if n == 1:
        #     return nums[0]
        counts = defaultdict(int)
        for i in nums:
            counts[i] += 1
            if counts[i] == 2:
                _ = counts.pop(i)
        return list(counts.keys())[0]

    def xor_solution(self, nums: List[int]) -> int:
        """
        Time complexity O(n) and space complexity should be O(1)
        """

        a = 0
        for num in nums:
            a ^= num

        return a


if __name__ == '__main__':
    sol = Solution()
    print(sol.singleNumber([4,1,2,1,2]))
    print(sol.singleNumber([4]))
    print(sol.singleNumber([2,2,1]))

    print(sol.xor_solution([4,1,2,1,2]))
    print(sol.xor_solution([4]))
    print(sol.xor_solution([2,2,1]))
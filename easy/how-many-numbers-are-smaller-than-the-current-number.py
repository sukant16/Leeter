from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        counter = {}
        sorted_nums = sorted(nums)
        res = []
        for i in range(len(sorted_nums)):
            sorted_num = sorted_nums[i]
            if sorted_num in counter:
                continue
            counter[sorted_num] = i

        for num in nums:
            res.append(counter[num])
        return res


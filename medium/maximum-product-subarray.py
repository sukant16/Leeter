from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)

        # dp1[i] keeps the maximum of sums of product till the ith index
        # dp2[i] keeps the minimum of sums of product till the ith index
        dp1 = [0]*n
        dp2 = [0]*n

        dp1[0] = dp2[0] = nums[0]

        for i in range(1, n):
            if nums[i] > 0:
                dp1[i] = max(dp1[i-1]*nums[i], nums[i])
                dp2[i] = min(dp2[i-1]*nums[i], nums[i])
            else:
                dp1[i] = max(dp2[i-1]*nums[i], nums[i])
                dp2[i] = min(dp1[i-1]*nums[i], nums[i])
        return max(dp1[i])
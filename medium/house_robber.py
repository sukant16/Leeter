# case: 2, 7, 9, 3, 1
# sum(2, 9, 1) > sum(7, 3, 1)
# i=0, (2,9), (2,3), (2,1) -> (2,9)
# i=1, (7,3), (7,1) -> (7,3)
# i=2, (9,1)

# case: 12, 1, 2, 10, 1
# sum(12, 10) > sum(1,2,1)
# i = 0, (12, 2), (12,10), (12,1)
# i = 1

from typing import List
from functools import lru_cache


class Solution:
    def rob(self, nums: List[int]) -> int:

        n = len(nums)

        @lru_cache()
        def helper(start):

            if start >= n:
                return 0

            return max(helper(start + 2), helper(start + 3)) + nums[start]

        return max(helper(0), helper(1))


    def rob_dp(self, nums: List[int]) -> int:
        dp1 = dp2 = 0

        for num in nums:
            dp1, dp2 = dp2, max(dp1 + num, dp2)
        return dp2


if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))
    print(sol.rob([2,7,9,3,1]))
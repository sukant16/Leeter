from typing import List
from math import floor
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = floor(len(nums)/3)
        counts = defaultdict(int)
        ans = set()
        for i in nums:
            counts[i] += 1
            if counts[i] > n:
                ans.add(i)
        return list(ans)


if __name__ == '__main__':
    sol = Solution()
    print(sol.majorityElement([3,2,3]))
    print(sol.majorityElement([1,1,1,3,3,2,2,2]))
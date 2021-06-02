from typing import List
from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        time complexity = O(n)
        space completxity = O(n)
        """
        x = defaultdict(int)
        for num in nums:  # Time complexity -> O(n)
            if num in x:  # Time complexity -> O(1)
                return True
            else:
                x[num] += 1
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
    print(sol.containsDuplicate([1, 2, 3, 4]))
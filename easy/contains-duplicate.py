from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        exists = False
        for i in range(len(nums)):
            n = min(i+k+1, len(nums))
            for j in range(i+1, n):
                if abs(nums[j] - nums[i]) <= t:
                    exists = True
                    break

        return exists


if __name__ == "__main__":
    sol = Solution()
    ans1 = sol.containsNearbyAlmostDuplicate([1,2,3,1], k=3, t=0)
    print(ans1)

    ans2 = sol.containsNearbyAlmostDuplicate(nums = [1,5,9,1,5,9], k = 2, t = 3)
    print(ans2)
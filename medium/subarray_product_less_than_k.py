from typing import List


class Solution:
    def brute_force(self, nums: List[int], k: int) -> int:
        ans = []
        for i in range(len(nums)):
            temp = 1
            j = i
            while (temp < k) and (j >= 0):
                if temp * nums[j] < k:
                    temp = temp * nums[j]
                    ans.append(temp)
                    j -= 1
                else:
                    break
        return len(ans)

    def numSubarrayProductLessThanK(self, nums, k):
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod /= nums[left]
                left += 1
            ans += right - left +1
        return ans


if __name__ == '__main__':
    sol = Solution()
    print(sol.numSubarrayProductLessThanK(nums = [10, 5, 2, 6], k = 100))

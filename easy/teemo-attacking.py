from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:

        if not timeSeries:
            return 0

        ans = 0
        n = len(timeSeries)
        for i in range(n-1):
            if timeSeries[i] + duration <= timeSeries[i+1]:
                ans += duration
            else:
                ans += timeSeries[i+1] - timeSeries[i]
        return ans + duration


if __name__ == '__main__':
    sol = Solution()
    print(sol.findPoisonedDuration([], 10))
    print(sol.findPoisonedDuration([1,4], 2))
    print(sol.findPoisonedDuration([1,2,3,4,5], 5))

    print(sol.short([], 10))
    print(sol.short([1,4], 2))
    print(sol.short([1,2,3,4,5], 5))



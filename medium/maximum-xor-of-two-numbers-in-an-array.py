from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:

        ans, mask = 0, 0
        for i in range(31, -1, -1):
            mask |= 1 << i

            found = {mask & num for num in nums}

            start = ans | 1 << i

            for prefix in found:
                if start^prefix in found:
                    ans = start
                    break

        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.findMaximumXOR([3, 10, 5, 25, 2, 8]))

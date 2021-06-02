from typing import List


class Solution:
    def reverse(self, x: int) -> int:
        num = i = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x // 10 > 0:
            num = num*10 + (x % 10)
            x = x//10
            i += 1
        return num * sign


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverse(-123))
    print(sol.reverse(110))
    print(sol.reverse(2**31))

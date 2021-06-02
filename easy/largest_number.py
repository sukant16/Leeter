from typing import List


class LargerNumKey(str):
    def __lt__(x, y):
        return x+y > y+x


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = "".join(sorted(map(str, nums), key=LargerNumKey))
        return '0' if largest_num[0] == '0' else largest_num


if __name__ == '__main__':
    sol = Solution()
    print(sol.largestNumber([3, 30]))
    print(sol.largestNumber([3,30,34,5,9]))
    print(sol.largestNumber([0,0,0,0,0]))